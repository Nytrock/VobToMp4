import glob
import ffmpeg
import os

if not os.path.exists("result"):
    os.mkdir("result")
list_ = []
for name in glob.glob("videos/*.VOB"):
    filename = name.split("\\")[1]
    result = "result/" + filename[0:filename.rfind(".")] + ".mp4"
    ffmpeg.input(name).output(result).run()
    os.system('cls')
    list_.append(filename + " - converted")
    print("\n".join(list_))
