# Discord YouTube Live Clipping Bot

A simple Discord clipping bot for YouTube livestreams. Right now it uploads to the CDN (which means it has a 25MB limit - I'm hoping to add some system to upload it somewhere else in the future! or maybe even compression... who knows)

# Demo

https://github.com/user-attachments/assets/b4305951-f7b9-4e4a-b81d-2d60833f3d14




# Requirements
- [ffmpeg](https://ffmpeg.org/download.html#build-windows) in PATH (or in the same directory as the bot)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp/releases/) in PATH (or in the same directory as the bot)
- [a fork of ytarchive (for now) with custom duration support](https://github.com/keredau/ytarchive/tree/feature/duration) in PATH or in the same directory as the bot - my compiled .exe can be found [here](https://github.com/Patrosi73/discord-youtubelive-clipping-bot/raw/main/ytarchive.exe) 

# Setup
1. Git Clone/Download the repository as a .zip
2. [Set up a Discord bot](https://www.xda-developers.com/how-to-create-discord-bot/) (follow guide until "assign bot function")
3. Create a file in the bot folder called `.env`. Inside it, put `TOKEN=(token)`, replacing (token) with your Discord bot token
4. Run `pip install discord.py` in a terminal
5. Run `python bot.py`. The bot will be online until you close the terminal.

# NOTICE
If you don't see any slash commands, ~~blame discord for making this system so dumb~~ run "!sync" in your server. When the bot responds with "Synced 1 commands globally", you should be able to see them now. If not, restart your client. If not, try running the command again.
