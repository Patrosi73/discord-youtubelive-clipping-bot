import os
import discord
import subprocess
import uuid
import asyncio
from compress import compress
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from utils import send_message

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
token = os.getenv("TOKEN")
max_duration = os.getenv("MAX_DURATION")
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)

async def setup_hook() -> None:
    await bot.tree.sync()
bot.setup_hook = setup_hook

@bot.command()
@commands.is_owner()
async def sync(ctx: commands.Context) -> None:
    """Sync commands"""
    synced = await ctx.bot.tree.sync()
    await ctx.send(f"Synced {len(synced)} commands globally")





@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

@bot.tree.command(name="clip", description="Clips a YouTube livestream",)
@app_commands.describe(link="The YouTube livestream to clip", seconds="The amount of seconds to clip", rewind="Rewind the specified amount of seconds - you probably want this")
async def clip(interaction: discord.Interaction, link: str, seconds: int, rewind: bool) -> None:

    link = link.split(" ")[0]
    print(link)
    await interaction.response.defer()
    max_duration_int = int(max_duration)
    if (seconds > max_duration_int):
        await send_message(interaction,f"Clip requested too large (max: {max_duration} seconds)")
        return

    async def run_command(command):
        # ChatGPT generated this for me :sunglasses_face:
        # still have no idea what black magic it actually does but it works. fuck it we ball
        process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return stdout.decode(), stderr.decode()


    try:

        stdout, _ = await run_command(["yt-dlp", link, "--print", "live_status"])
        live_status = stdout.strip()
    except Exception as e:
        last_line = e.args[0].strip().split('\n')[-1]
        await send_message(interaction,f"Failed to check live status: ```ansi\n{str(last_line)}```")
        return

    match live_status:
        case "not_live":
            await send_message(interaction, f"{link} is not a livestream")
        case "is_live":
            randomuuid = str(uuid.uuid4())
            if rewind:
                await interaction.followup.send(f"Downloading the last {seconds} seconds of stream...")
                download_command = [
                    "ytarchive",
                    f"-o", randomuuid, f"--live-from", f"-{seconds}s", f"--capture-duration", f"{seconds}s",
                    link, "best"
                ]
            else:
                await interaction.followup.send(f"Downloading stream for {seconds} seconds...")
                download_command = [
                    "ytarchive",
                    f"-o", randomuuid, f"--live-from", "now", f"--capture-duration", f"{seconds}s",
                    link, "best"
                ]
            
            try:
                stdout, stderr = await run_command(download_command)
                if "Final file" not in stdout and "Final file" not in stderr:
                    raise Exception(stderr)
            except Exception as e:
                last_line = e.args[0].strip().split('\n')[-1]
                await send_message(interaction, f"Failed to download: {str(last_line)}")
                return

            clip_filename = f"{randomuuid}.mp4"
            clip_filename_compressed = f"25MB_{randomuuid}.mp4"
            if (os.path.getsize(clip_filename) > 25165824):
                await send_message(interaction, f"Download finished. Output file too large for Discord, compressing and uploading...")
                await compress(clip_filename, seconds)
                file = discord.File(clip_filename_compressed, filename=f"clip_{randomuuid}.mp4")
                await interaction.followup.send(file=file)
                os.remove(clip_filename)
                os.remove(clip_filename_compressed)
            else:
                await send_message(interaction, f"Download finished, uploading...")
                file = discord.File(clip_filename, filename=f"clip_{randomuuid}.mp4")
                await interaction.followup.send(file=file)
                os.remove(clip_filename)
            
        case "is_upcoming":
            await send_message(interaction,"`{link}` is an upcoming stream, cannot clip something that doesn't exist yet ;)")
        case "was_live":
            await send_message(interaction,"`{link}` is no longer live")
        case "post_live":
            await send_message(interaction,"`{link}` is no longer live and isn't yet processed. You just missed it :(")
        case _:
            await send_message(interaction,"Unknown live status: `{live_status}`")

bot.run(token)