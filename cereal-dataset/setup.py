# set up folders and file paths 
import os 
dirs = ["data-raw", "data-output", "resources", "notebooks"]

[os.mkdir(dir) for dir in dirs if not os.path.isdir(dir)]