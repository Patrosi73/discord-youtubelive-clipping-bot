@echo off
echo This script assumes you have already installed Python 3.8 or higher and have it in PATH. If you're not sure, reinstall Python from https://www.python.org/downloads/
echo This script also assumes that you have a 64-bit PC. If you don't, you probably know what you're doing and this script isn't for you.
echo MAKE SURE YOU ARE *NOT* RUNNING THIS AS ADMINISTRATOR!
pause
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/Patrosi73/discord-youtubelive-clipping-bot/blob/main/ytarchive.exe', 'ytarchive.exe')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe', 'yt-dlp.exe')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip', 'ffmpeg.zip')"
powershell -Command "Expand-Archive -Path '.\ffmpeg.zip' -DestinationPath '.\ffmpeg\'"
copy .\ffmpeg\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe .\ffmpeg.exe
pip install discord.py python-dotenv
