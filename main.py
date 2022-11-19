import glob
import stat

import ffmpeg
import os


def main():
    # Start message
    if not confirm_working('Welcome to VOB to mp4 converter. All ".VOB" files in the "video" folder will be '
                           'converted to ".mp4" and placed in the "results" folder. '
                           'Nothing will happen to the original files. And please do not interrupt the program! '
                           '\nClear?', True):
        write_to_console("The program has been interrupted.")
        return

    # Check for "videos" folder
    if not os.path.exists("videos"):
        write_to_console('Error: Folder "videos" not found. Please create it in the same place where the '
                         'application is located and place the files for conversion there.')
        os.mkdir("videos")
        return

    # Creating or cleaning "result" folder
    if not os.path.exists("result"):
        os.mkdir("result")
    else:
        if len([f for f in os.listdir("result")]) != 0:
            if confirm_working('Files were found in the "results" folder. For the correct operation '
                               'of the program, they will have to be removed.'):
                clean_trash("result")
            else:
                write_to_console("The program has been interrupted.")
                return

    # Converting from VOB to mp4
    write_to_console("Starting the conversion... Don't be afraid to see a lot of text next..", True)
    for name in glob.glob("videos/*.VOB"):
        filename = name.split("\\")[1]
        result = "result/" + filename[0:filename.rfind(".")] + ".mp4"
        ffmpeg.input(name).output(result, ac=2).run()
    write_to_console("All files have been successfully converted")


# Write something to the console
def write_to_console(text: str, end=False) -> None:
    os.system('cls')
    if end:
        print(text)
    else:
        print(text, end='')


# Confirmation of any action
def confirm_working(text: str, full=False) -> bool:
    os.system('cls')
    if full:
        print(f"{text} (n/y)")
    else:
        print(f"{text} Continue? (n/y)")
    while True:
        answer = input()
        if answer == "n":
            return False
        elif answer == "y":
            return True
        else:
            print("Enter the correct answer (n - no, y - yes)")


# Removing all files from the "videos" folder
def clean_trash(path: str) -> None:
    dirlist = [f for f in os.listdir(path)]
    for f in dirlist:
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            clean_trash(fullname)
            os.rmdir(fullname)
        else:
            os.chmod(fullname, stat.S_IWRITE)
            os.remove(fullname)


# Start
if __name__ == '__main__':
    main()
