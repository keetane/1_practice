import ffmpy
ff = ffmpy.FFmpeg(
inputs = {'/Users/keetane/Documents/code/FROZEN  Let It Go Sing-along  Official Disney UK.mp4' :None},
outputs = {'output.mp3' :None}
)
ff.run()