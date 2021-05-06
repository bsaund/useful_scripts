#! /usr/bin/env python

COMMON_COMMANDS = """
Compress video:
ffmpeg -i input.mp4 -vcodec libx265 -crf 28 output.mp4
(Note: higher crf = more compression. Slack does not like libx265, use libx264)

All files in directory
for i in *.avi; do ffmpeg -i "$i" "${i%.*}.mp4"; done

Convert to gif: 
ffmpeg -i input.MP4 -vf "scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" output.gif
"""


if __name__ == '__main__':
    print("These are some common ffmpeg commands I use")
    print(COMMON_COMMANDS)

