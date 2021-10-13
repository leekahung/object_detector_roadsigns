#!/bin/bash

# Get video from YouTube
ffmpeg $(youtube-dl -g 'https://www.youtube.com/watch?v=vKD8_m88tuk' | sed "s/.*/-ss 1700 -i &/") -t 30 -c copy -vcodec mpeg4 test_video.mkv

# Convert mkv to mp4
ffmpeg -i test_video.mkv -codec copy test_video.mp4
