# Discord YouTube Live Clipping Bot

A simple Discord clipping bot for YouTube livestreams. The clip is uploaded to the Discord CDN (and if it doesn't fit under 25MB, it's compressed and then uploaded. rclone uploads are planned)

# Demo

https://github.com/user-attachments/assets/a48e28f3-11fc-4cc6-ae3e-c14dd7167597


# Requirements
- [Python 3.8+](https://www.python.org/downloads/) in PATH
- [ffmpeg](https://ffmpeg.org/download.html#build-windows) in PATH (or in the same directory as the bot)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp/releases/) in PATH (or in the same directory as the bot)
- [a fork of ytarchive (for now) with custom duration support](https://github.com/keredau/ytarchive/tree/feature/duration) in PATH or in the same directory as the bot - my compiled .exe can be found [here](https://github.com/Patrosi73/discord-youtubelive-clipping-bot/raw/main/ytarchive.exe) 

# Setup
0. Make sure you have all the requirements installed.
> [!NOTE]
> For Windows users, please check if Python is in PATH. And make sure to run Python correctly as most times it's `py` or `python3` instead of `python`. In this guide, This will be referred to as `python` at the start of the command.
1. Git Clone/Download the repository as a .zip and extract it.
> [!NOTE]
> When inviting the bot to your server, make sure the bot has "Message Intent" and "Application Command" scope on when you are making an invite link.
2. If you don't know what a bot token is, follow the guide in [Add Bot Readme File](/ADD-BOT.md) if you don't know what this means. If you do, create a bot at the [Discord Developer Portal](https://discord.com/developers/applications)
> [!IMPORTANT]
> Do NOT forget to turn on "Message Content Intent" and in the Bot settings.
3. Run `pip install discord.py python-dotenv` in a terminal
> [!NOTE]
> You might not have `pip` installed but you can try running `python -m pip install discord.py python-dotenv`  instead.
4. Run `python bot.py` once.
5. The program will create a `.env` file in the same directory as the bot. Add your bot token to the file replacing the "(token)". Also, set maximum duration of the clip in seconds (default is 100 seconds), should you want to change it.
> [!NOTE]
> If you followed the guide, it's the thing you copied after you reset token.
6. Run `python bot.py` again.

# NOTICE
If you don't see any slash commands, ~~blame discord for making this system so dumb~~ run "!sync" in your server. When the bot responds with "Synced 1 commands globally", you should be able to see them now. If not, restart your client. If not, try running the command again.
