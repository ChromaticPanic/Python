import os
import csv
import sys
import pandas as pd
from fuzzywuzzy import process

def main():
    inPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    fileName = "14_Councilv2.csv"
    inFile = inPath + fileName
    outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    outfile = outPath + "14_Councilv3.csv"

    hoodsFile = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\" + "12_Company_address_updatedv2.csv"
    
    hoods = pd.read_csv(hoodsFile)

    if not os.path.isfile(inFile):
        input("Press any key to exit")
        sys.exit(1)
    
    df = pd.read_csv(inFile)
    outdf = pd.merge(df, hoods, how='left', left_on='vendor', right_on='name')
    print(outdf.head())
            
    outdf.to_csv(outfile, index=False)
    sys.exit(0)


if __name__ == "__main__":
    main()