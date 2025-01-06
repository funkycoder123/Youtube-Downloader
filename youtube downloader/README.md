YouTube Downloader

A Python-based YouTube video downloader using yt-dlp and FFmpeg. This script downloads videos in the desired resolution and merges them into an MP4 file.

Features

Download YouTube videos.

Merge video and audio streams using FFmpeg.

Specify output directory and resolution.

Requirements

Python 3.6 or higher

yt-dlp (install using pip install yt-dlp)

FFmpeg (must be installed and in PATH)

Installation

Clone the repository:

git clone ....
cd youtube-downloader

Install dependencies:

pip install -r requirements.txt

Usage

Run the script with:

python downloader.py -u "https://youtu.be/example" -o "./Downloads" -r 1080

-u or --url: YouTube video URL (required).

-o or --output: Output directory for the downloaded video (default: ./Downloads).

-r or --resolution: Preferred video resolution (e.g., 720, 1080; default: 1080).

Example

Download a video to the Downloads folder in 720p resolution:

python downloader.py -u "https://youtu.be/example" -o "./Downloads" -r 720

License

This project is licensed under the MIT License. See LICENSE for details.
