import os
import shutil as sh

dir = ".\\sounds"
files = []

for filename in os.listdir(dir):
    if filename.split(".")[1] == "mp3":
        files.append(filename)

print(files)