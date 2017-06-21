from os import path,listdir,mkdir
from os.path import isfile,join
dirname = "/home/bobi/Downloads"
files = [name for name in listdir(dirname) if isfile(join(dirname, name))]

dirfiles = [dirname + "/" + s for s in files]

for i in dirfiles:print(round((path.getsize(i)/pow(1024,2)),4),"MB")

#print(dirfiles)