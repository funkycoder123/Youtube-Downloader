import subprocess
import shutil
import argparse
import os


def check_ffmeg():
    if not shutil.which("yt-dlp"):
        print(
            "FFmpeg is not installed or not in PATH. Please install it before running the script."
        )
        exit(1)


def downloader(url, resolution, output):
    try:
        # Command to download the best video and audio quality
        command = [
            "yt-dlp",
            "-f",
            f"bestvideo[height<={resolution}]+bestaudio/best",
            "--merge-output-format",
            "mp4",  # Merge and save as MP4
            "--ffmpeg-location",
            shutil.which("ffmpeg"),
            "-o",
            os.path.join(output, "%(title)s.%(ext)s"),  # Save as title.extension
            url,
        ]
        # Execute the command
        subprocess.run(command, check=True)
        print("Video downloaded successfully in the best quality!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("-u", "--url", required=True, help="YouTube video URL")
    parser.add_argument("-o", "--output", default=".", help="Output directory")
    parser.add_argument(
        "-r",
        "--resolution",
        default="1080",
        help="Preferred video resolution (e.g., 720, 1080)",
    )
    args = parser.parse_args()

    # Ensure output directory exists
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    check_ffmeg()
    downloader(args.url, args.resolution, args.output)


if __name__ == "__main__":
    main()
