import os
import sys
import subprocess as sp

#os.chdir("F:\\Uni Files\\3380\\FDTool")

def main():
    inPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"

    #directory = os.fsencode(inPath)
    for file in os.listdir(inPath):
        print("fdtool" + " " + os.path.abspath(file))
        sp.run("fdtool" + " " + "\"" + os.path.abspath(file) + "\"", shell=True)

    #input("Press any key to exit")
    sys.exit(0)


if __name__ == "__main__":
    main()