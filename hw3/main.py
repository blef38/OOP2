from importlib.metadata import files
from os import write

import os
file_path = os.path.realpath(__file__)
script_dir = os.path.dirname(file_path)
directory = os.path.join(script_dir,"source") #файлы исходники лежат в папке source
files_list = os.listdir(directory)

file_lens_dict = {}
for f_name in files_list:
    with open(os.path.join(directory,f_name), encoding="utf-8") as fp:
        x1 = len(fp.readlines())
        file_lens_dict[f_name] = x1

sorted_f = dict(sorted(file_lens_dict.items(), key=lambda item: item[1]))

with (open('summary.txt', "w+", encoding="utf-8") as fp):
    for k in sorted_f:
        fp.writelines(k+"\n")
        fp.write(str(sorted_f[k])+"\n")
        with (open(os.path.join(directory,k), "r+", encoding="utf-8") as fr):
            tex = fr.readlines()
        fp.writelines(tex)
        fp.write("\n")

