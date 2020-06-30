#! /usr/bin/python3
import os
print("Git clone tool 0.1 Alpha")
while True:
    try:
        print("Gitclone > ",end="")
        res = str(input())
        if res == "exit":
            exit(1)
        elif res == "dir":
            os.system("dir")
        elif res == "tree":
            os.system("tree")
        else:
           os.system("git clone " + res) 
    except KeyboardInterrupt:
        print()
        pass
    except EOFError:
        print("exit")
        exit(1)
