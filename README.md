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
1. Git Clone/Download the repository as a .zip
> [!NOTE]
> When inviting the bot to your server, make sure the bot has "Message Intent" and "Application Command" scope on when you are making an invite link.
2. If you do not have a bot token, create a bot at the [Discord Developer Portal](https://discord.com/developers/applications) or follow the guide in [Add Bot Readme File](/ADD-BOT.md)
3. Run `pip install discord.py python-dotenv` in a terminal
4. Run `python bot.py`. The bot will be online until you close the terminal.
5. 

# NOTICE
If you don't see any slash commands, ~~blame discord for making this system so dumb~~ run "!sync" in your server. When the bot responds with "Synced 1 commands globally", you should be able to see them now. If not, restart your client. If not, try running the command again.
