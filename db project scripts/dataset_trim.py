import os
import csv
import sys
import pandas as pd
import numpy as np

def main():
   fileName = "F:\\Uni Files\\3380\\code\\A3\\2_Council_Member_Expenses.csv"
   #filename = "2_Council_Member_Expenses.csv"
   outfile = "F:\\Uni Files\\3380\\code\\A3\\2_Council_Member_Expenses_trim.csv"
   if not os.path.isfile(fileName):
      input("Press any key to exit")
      sys.exit(1)

   df = pd.read_csv(fileName)
   df.drop(df.loc[df['Journal Date'].str.contains("2014")].index, inplace=True)
   df.drop(df.loc[df['Journal Date'].str.contains("2015")].index, inplace=True)
   df.drop(df.loc[df['Journal Date'].str.contains("2016")].index, inplace=True)
   df.drop(df.loc[df['Journal Date'].str.contains("2017")].index, inplace=True)
   df.drop(df.loc[df['Journal Date'].str.contains("2018")].index, inplace=True)
   df.drop(df.loc[df['Journal Date'].str.contains("2019")].index, inplace=True)
   #df.drop(df.loc[df['Journal Date'].str.contains("2021")].index, inplace=True)
   df.drop(df.loc[df['Amount'].str.replace(',','').astype(float)<100].index, inplace=True)
   df.drop(df.loc[df['Description'].str.contains("Salary")].index, inplace=True)
   df.drop(df.loc[df['Vendor'].str.contains("Journal")].index, inplace=True)
   df.to_csv(outfile, index=False)
   print(df.to_string())
   


if __name__=="__main__":
   main()