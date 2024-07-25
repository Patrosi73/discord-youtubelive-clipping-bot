import subprocess
import asyncio
from bot import send_message
# this is mostly stolen code from https://github.com/MyloBishop/discompress because i was too lazy to figure out compression stuff myself haha
async def run_command(command):
        process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return stdout.decode(), stderr.decode()

async def compress(inputfile, duration):
    bitrate = 23 * 8 * 1000 / duration
    video_bitrate = bitrate * 90 / 100
    audio_bitrate = bitrate * 10 / 100
    command = [
    "ffmpeg",
    "-hide_banner",
    "-loglevel", "warning",
    "-stats",
    "-hwaccel", "auto",
    "-i", inputfile,
    "-c:v", "h264_nvenc",
    f"-b:v", f"{video_bitrate}k",
    "-c:a", "aac",
    f"-b:a", f"{audio_bitrate}k",
    f"-bufsize", f"{bitrate}k",
    "-minrate", "100",
    f"-maxrate", f"{bitrate}k",
    f"25MB_{inputfile}"
    ]
    try:
        await run_command(command)
    except Exception as e:
        last_line = e.args[0].strip().split('\n')[-1]
        await send_message(f"Failed to compress: {str(last_line)}")
        