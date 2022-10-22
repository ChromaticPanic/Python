import os
import csv
import sys
import pandas as pd
from fuzzywuzzy import process

def main():
    inPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    fileName = "14_Council_Member_Expenses_updatedv2.csv"
    inFile = inPath + fileName
    outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    outfile = outPath + "14_Councilv2.csv"

    hoodsFile = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\" + "12_Company_address_updatedv2.csv"
    
    hoods = pd.read_csv(hoodsFile)

    if not os.path.isfile(inFile):
        input("Press any key to exit")
        sys.exit(1)
    
    df = pd.read_csv(inFile)
  
    for i in df.index:
        topMatch = process.extractOne(df.loc[i, 'vendor'], hoods['name'])
        if topMatch[1] > 90 and topMatch[1] < 100:
            print(i, "of", df.index.size)
            print(topMatch[0], topMatch[1], df.loc[i, 'vendor'])
            df.loc[i, 'vendor'] = topMatch[0]
            
    df.to_csv(outfile, index=False)
    sys.exit(0)


if __name__ == "__main__":
    main()