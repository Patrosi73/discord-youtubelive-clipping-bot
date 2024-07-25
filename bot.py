import os
import discord
import subprocess
import glob
import uuid
import asyncio
from compress import compress
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
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


async def check_live_status(link: str):
    try:
        live_status = subprocess.check_output(["yt-dlp", link, "--print", "live_status"], text=True).strip()
        return live_status
    except:
        return None

@bot.tree.command(name="clip", description="Clips a YouTube livestream",)
@app_commands.describe(link="The YouTube livestream to clip", seconds="The amount of seconds to clip", rewind="Rewind the specified amount of seconds - you probably want this")
async def clip(interaction: discord.Interaction, link: str, seconds: int, rewind: bool) -> None:

    await interaction.response.defer()
    max_duration_int = int(max_duration)
    if (seconds > max_duration_int):
        await interaction.followup.send(f"Clip requested too large (max: {max_duration} seconds)")
        return

    live_status = await check_live_status(link)
    if live_status is None:
        await interaction.followup.send(f"Failed to check live status.")
        return
    match live_status:
        case "not_live":
            await interaction.followup.send(f"`{link}` is not a livestream")
        case "is_live":
            randomuuid = str(uuid.uuid4())
            if (rewind):
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
                subprocess.call(download_command)
            except:
                await interaction.followup.send(f"Failed to download.")
                return
            
            clip_filename = f"{randomuuid}.mp4"
            clip_filename_compressed = f"25MB_{randomuuid}.mp4"
            if (os.path.getsize(f"{randomuuid}.mp4") > 25165824):
                await interaction.followup.send(f"Download finished. Output file too large for Discord, compressing and uploading...")
                compress(clip_filename, seconds)
                file = discord.File(clip_filename_compressed, filename=f"clip_{randomuuid}.mp4")
                await interaction.followup.send(file=file)
            else:
                await interaction.followup.send(f"Download finished, uploading...")
                file = discord.File(clip_filename, filename=f"clip_{randomuuid}.mp4")
                await interaction.followup.send(file=file)
            
        case "is_upcoming":
            await interaction.followup.send(f"`{link}` is an upcoming stream, cannot clip something that doesn't exist yet ;)")
        case "was_live":
            await interaction.followup.send(f"`{link}` is no longer live")
        case "post_live":
            await interaction.followup.send(f"`{link}` is no longer live and isn't yet processed. You just missed it :(")
        case _:
            await interaction.followup.send(f"Unknown live status: `{live_status}`")
bot.run(token)
