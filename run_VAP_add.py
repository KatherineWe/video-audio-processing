# Function: Add audio to video.

# Note:
#     The input video should contain no audio.
#     If it contains audio, new audio will not be added.

import os
import subprocess


# Set the path of input and output files.
INPUT_VIDEO = "Media/VideoDemo1080P.mp4"
INPUT_AUDIO = "Media/VideoDemo.wav"
OUTPUT_FILE = "Media/VideoDemo1080P_S.mp4"

# Check if the output file exists. If so, delete it.
if os.path.isfile(OUTPUT_FILE) is True:
    os.remove(OUTPUT_FILE)

# Set the command for processing the input video/audio.
cmd = "ffmpeg -i " + INPUT_VIDEO + " -i " + INPUT_AUDIO + " -c:v copy -c:a aac -strict experimental " + OUTPUT_FILE

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)
