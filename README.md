# Discord YouTube Live Clipping Bot

A simple Discord clipping bot for YouTube livestreams. The clip gets downloaded with a random UUID filename and is either:
- uploaded to the Discord CDN (if it's below 25MB),
- compressed and uploaded to the Discord CDN (if above 25MB),
- or uploaded to an [rclone destination](https://rclone.org/overview/) and the link for it shared to Discord (also if above 25MB, this is not default and has to be optionally set up).

# Demo

https://github.com/user-attachments/assets/a48e28f3-11fc-4cc6-ae3e-c14dd7167597


# Requirements
> [!NOTE]
> If you're on a Windows PC, I've made a script that automatically downloads everything for you (except for Python which you have to install yourself). Run **setup-for-windows.bat**
- [Python 3.8+](https://www.python.org/downloads/) in PATH
- [ffmpeg](https://ffmpeg.org/download.html#build-windows) in PATH (or in the same directory as the bot)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp/releases/) in PATH (or in the same directory as the bot)
- [a fork of ytarchive (for now) with custom duration support](https://github.com/keredau/ytarchive/tree/feature/duration) in PATH or in the same directory as the bot - my compiled .exe can be found [here](https://github.com/Patrosi73/discord-youtubelive-clipping-bot/raw/main/ytarchive.exe) , or [compile it yourself](/COMPILING-YTARCHIVE.md)

# Setup
0. Make sure you have all the requirements installed.
> [!NOTE]
> For Windows users, please check if Python is in PATH. And make sure to run Python correctly as most times it's `py` or `python` instead of `python3` (at least on Windows systems). In this guide, this will be referred to as `python` at the start of the command.
1. Git Clone/Download the repository as a .zip and extract it.
2. <span style="font-size:1.5rem;font-weight:900">If you don't know what a bot token is, follow the guide in [Add Bot Readme File](/ADD-BOT.md). </span>
If you do, create a bot at the [Discord Developer Portal](https://discord.com/developers/applications).
> [!IMPORTANT]
> Do NOT forget to turn on "Message Content Intent" and in the Bot settings and "Application Command" scope in OAuth2 settings.

3. Run `pip install discord.py python-dotenv` in a terminal
> [!NOTE]
> If it says `pip is not found` or something like that, `pip` is probably not installed (somehow). Either you reinstall Python with `pip` or follow this [guide](https://pip.pypa.io/en/stable/installation/) to install `pip`.
> Alternatively, running `python -m pip install discord.py python-dotenv`  instead. It might be that your system doesn't have `pip` in PATH.
4. Run `python bot.py` once.
5. The program will create a `.env` file in the same directory as the bot. Add your bot token to the file replacing the "(token)". Also, set maximum duration of the clip in seconds (default is 180 seconds), should you want to change it.
> [!NOTE]
> If you followed the guide, it's the thing you copied after you reset token.
6. Run `python bot.py` again. The bot should be up and running now.
> 
# NOTICE
If you don't see any slash commands, ~~blame discord for making this system so dumb~~ run "!sync" in your server. When the bot responds with "Synced 1 commands globally", you should be able to see them now. If not, restart your client. If not, try running the command again.

# Rclone setup
On some low-end systems and in some scenarios, compression can be a dealbreaker, whether it's because of the speed or for the sake of preserving quality. This is why the bot supports [rclone](https://rclone.org/overview/), so instead of uploading the clip to Discord, it uploads to an rclone destination and shares a link to the file.
The usage of rclone is optional - if it isn't set up, the bot defaults to using compression.
## Requirements
- [rclone](https://rclone.org/downloads/) in PATH
- Either a remote already added, or if you're copying it to a local directory (e.g if you're hosting an HTTP server on the same machine) the folder where all of your clips will reside
1. Open the .env file. Here you'll be entering your rclone configuration:
   
![image](https://github.com/user-attachments/assets/a335c650-a3c9-43e9-9bbb-e25e70da2e2f)

2. Set `USE_RCLONE` to `yes`
3. Set `RCLONE_REMOTE_NAME` to either:
   - the name of your remote, appended with `:/`
   - the folder of your HTTP server where your clips will reside
     
![oltO6mQ2Rn](https://github.com/user-attachments/assets/0eba5cee-9a37-4dab-87f3-ef8ce0b80ff6)

4. If you're uploading to a simple remote (e.g Google Drive), this is as far as you need to go. However if you're uploading to an HTTP server (e.g through an SFTP remote or locally), set `USE_RCLONE_LINK` to `no` and set `CUSTOM_LINK` to your domain and folder where the clips will be available.

![image](https://github.com/user-attachments/assets/67c5c6b7-cf53-46ce-9d32-a719467ce9d2)


   


