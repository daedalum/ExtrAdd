from os import system, listdir, mkdir
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()


###
print('\033[1;32m-*' * 19)
print("""
 ___       _         ___     _     _ 
| __|__ __| |_  _ _ /   \ __| | __| |
| _| \ \ /|  _|| '_|| - |/ _` |/ _` |
|___|/_\_\ \__||_|  |_|_|\__/_|\__/_|
\n""")
print('-*' * 19 + '\033[m')
print()


###
print("• Please, select the folder where are the videos whose audio you want to extract.")
path_ex_audio = filedialog.askdirectory(title="Select the folder where are the videos whose audio you want to extract")

list_ex_audio = listdir(path_ex_audio)
list_ex_audio.sort()

mkdir(f"{path_ex_audio}/Extract")

for p, v in enumerate(list_ex_audio):
    system(f'ffmpeg -i "{path_ex_audio}/{v}" -vn -acodec copy "{path_ex_audio}/Extract/{p+1:02d}.aac"')


###
print("• Now, select the folder with the videos you want to add the audios to.")
path_og_video = filedialog.askdirectory(title="Select the folder with the videos you want to add the audios to")

list_og_video = listdir(path_og_video)
list_new_audio = listdir(f"{path_ex_audio}/Extract/")

list_new_audio.sort()
list_og_video.sort()

mkdir(f"{path_og_video}/Modified")

for p, v in enumerate(list_og_video):
    system(f'ffmpeg -i "{path_og_video}/{v}" -i "{path_ex_audio}/Extract/{list_new_audio[p]}" -map 0 -map 1:a -c:v copy -sn -shortest "{path_og_video}/Modified/{p+1:02d}.mkv"')
