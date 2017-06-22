import os

def printdircontents(path):
    for child in os.listdir(path):
        childpath = os.path.join(path,child)
        if os.path.isdir(childpath):
            printdircontents(childpath)
        else:
            print(childpath)

printdircontents("/home/bobi")