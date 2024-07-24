import subprocess
# this is mostly stolen code from https://github.com/MyloBishop/discompress because i was too lazy to figure out compression stuff myself haha
def compress(inputfile, duration):
    bitrate = 23 * 8 * 1000 / duration
    video_bitrate = bitrate * 90 / 100
    audio_bitrate = bitrate * 10 / 100
    command = [
    "ffmpeg",
    "-hide_banner",
    "-loglevel", "warning",
    "-stats",
    "-threads", "0",
    "-hwaccel", "auto",
    "-i", inputfile,
    "-preset", "slow",
    "-c:v", "h264_nvenc",
    f"-b:v", f"{video_bitrate}k",
    "-c:a", "aac",
    f"-b:a", f"{audio_bitrate}k",
    f"-bufsize", f"{bitrate}k",
    "-minrate", "100",
    f"-maxrate", f"{bitrate}k",
    f"25MB_{inputfile}"
    ]
    subprocess.call(command)