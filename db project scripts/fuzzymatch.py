import os
import csv
import sys
import pandas as pd
from fuzzywuzzy import process
import multiprocessing as mp


def main():
    inPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    fileName = "11_Crime_Year_to_Date_Full_Data_data_updatedv2.csv"
    inFile = inPath + fileName
    outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    outfile = outPath + "11_Crimev2.csv"

    hoodsFile = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\" + "20_hood_ward_sch_dist.csv"
    
    hoods = pd.read_csv(hoodsFile)

    if not os.path.isfile(inFile):
        input("Press any key to exit")
        sys.exit(1)
    
    df = pd.read_csv(inFile)
  
    pool = mp.Pool(mp.cpu_count()/2)
    for i in df.index:
        topMatch = process.extractOne(df.loc[i, 'neighbourhood'], hoods['neighbourhood'])
        df.loc[i, 'neighbourhood'] = topMatch[0]
        if i % 500 == 0:
            print(i, "of", df.index.size)
            print(topMatch[0], df.loc[i, 'neighbourhood'])
            
    df.to_csv(outfile, index=False)
    sys.exit(0)


if __name__ == "__main__":
    main()