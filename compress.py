import subprocess
import asyncio
import os
from utils import send_message

async def run_command(command):
    process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return stdout.decode(), stderr.decode()

async def compress(inputfile, duration):
    print(f"Starting compression for {inputfile}")
    bitrate = 23 * 8 * 1000 / duration
    video_bitrate = bitrate * 90 / 100
    audio_bitrate = bitrate * 10 / 100
    outputfile = f"25MB_{inputfile}"
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "warning",
        "-stats",
        "-i", inputfile,
        "-c:v", "libx264",
        f"-b:v", f"{video_bitrate}k",
        "-c:a", "aac",
        f"-b:a", f"{audio_bitrate}k",
        f"-bufsize", f"{bitrate}k",
        "-minrate", "100",
        f"-maxrate", f"{bitrate}k",
        outputfile
    ]
    try:
        stdout, stderr = await run_command(command)
        print(f"FFmpeg stdout: {stdout}")
        print(f"FFmpeg stderr: {stderr}")

        if not os.path.exists(outputfile):
            raise Exception("Output file was not created")

    except Exception as e:
        last_line = str(e).strip().split('\n')[-1]
        await send_message(f"Failed to compress: {str(last_line)}")
        print(f"Failed to compress: {str(last_line)}")