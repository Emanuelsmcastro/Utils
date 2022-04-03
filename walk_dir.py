from os import listdir
from os.path import isfile, join
path = 'C:/Users/darkt/Desktop/pythonProject1'
files = [f for f in listdir(path) if isfile(join(path, f))]
print(files)
