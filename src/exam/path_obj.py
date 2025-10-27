import glob
import os
import shutil


print("Current working directory: %s" % os.getcwd())

current_file = os.getcwd()

parent_directory = os.path.dirname(current_file)

print("Parent directory of current file: %s" % parent_directory)


print("basename : ", os.path.basename(current_file)) 

for file_path in glob.glob("src/%s/*.py" % current_file):
    parent_dir = os.path.dirname(file_path)
    print("Parent directory of %s: %s" % (file_path, parent_dir))


import collections, pathlib
Counter = collections.Counter([p.suffix for p in pathlib.Path.cwd().iterdir()])
print(Counter)
# Counter({'.md': 2, '.txt': 4, '.pdf': 2, '.py': 1})

