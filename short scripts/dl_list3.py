import os
import multiprocessing as mp
import subprocess as sp
import time
import random as rd

dname = os.path.abspath(os.path.dirname(__file__))
os.chdir(dname)

completed = []


def main():
    fileName = 'dl.txt'

    #pool = mp.Pool(mp.cpu_count())
    pool = mp.Pool(processes=4)

    with open(fileName, "r") as file:
        lines = file.readlines()
        pool.map(getFile, lines)

    input("Press Any key to exit")


def getFile(inputLine):
    time.sleep(rd.randint(1000, 10000)/1000)

    if inputLine not in completed:
        completed.append(inputLine)
        p = sp.Popen(["yt-dlp.exe ", inputLine, "-w", "--restrict-filenames",
                     "--windows-filenames"], creationflags=sp.CREATE_NEW_CONSOLE)
        p.wait()
        print(inputLine + " done")


if __name__ == "__main__":
    main()
