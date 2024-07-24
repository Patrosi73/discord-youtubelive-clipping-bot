import os
import discord
import subprocess
import glob
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
token = os.getenv("TOKEN")
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

@bot.tree.command(name="clip", description="Clips a YouTube livestream")
@app_commands.describe(link="The YouTube livestream to clip", seconds="The amount of seconds to clip")
async def clip(interaction: discord.Interaction, link: str, seconds: int) -> None:
    download_command = [
    "yt-dlp",
    f"--downloader-args", f"ffmpeg:-t {seconds}",
    link
]
    await interaction.response.defer()
    try:
        live_status = subprocess.check_output(["yt-dlp", link, "--print", "live_status"], text=True).strip()
    except subprocess.CalledProcessError as e:
        await interaction.followup.send(f"Failed to check live status.")
        return
    match live_status:
        case "not_live":
            await interaction.followup.send(f"`{link}` is not a livestream")
        case "is_live":
            await interaction.followup.send(f"Downloading stream for {seconds} seconds...")
            try:
                subprocess.call(download_command)
            except subprocess.CalledProcessError as e:
                await interaction.followup.send(f"Failed to download.")
                return
            
            list_of_files = glob.glob('.\\*.mp4')
            newest = max(list_of_files, key=os.path.getctime)
            just_file_name = newest.split('\\')[-1]

            await interaction.followup.send(f"Download finished, uploading... \n -# if you don't see the clip after some time, the upload has failed. you can find it in the bot's folder")
            file = discord.File(just_file_name, filename="clip.mp4")
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
