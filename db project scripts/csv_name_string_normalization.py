import os
import csv
import sys
import json
import pandas as pd


def main():
    inPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    fileName = "22_Park_Asset_Inventory_updated.csv"
    inFile = inPath + fileName
    outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    outfile = outPath + fileName[:-4] + "v2.csv"

    if not os.path.isfile(inFile):
        input("Press any key to exit")
        sys.exit(1)
    cols = ['park name', 'asset class', 'asset type']
    df = pd.read_csv(inFile)
    #df.rename(columns = {'ED':'name'}, inplace = True)
    #df.drop(columns = ['ED_French','Type','SHAPE_Leng', 'SHAPE_Area'], inplace = True)
    df.columns = df.columns.str.lower()
    for col in cols:
        df[col] = df[col].str.strip()
        df[col] = df[col].str.replace('[^a-zA-Z0-9]', ' ', regex = True).str.lower()
        df[col] = df[col].str.replace('\s+', ' ', regex = True)
    print(df)


    df.to_csv(outfile, index=False)

    #input("Press any key to exit")
    sys.exit(0)


if __name__ == "__main__":
    main()
