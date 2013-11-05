import os

cwd = os.getcwd()

def list(path):
    rez = []
    for f in os.listdir(path):
        f = os.path.join(path, f)
        if os.path.isdir(f):
            f = list(f)
        elif os.path.splitext(f)[1] == '.py':
            print("*",f)
list(cwd)