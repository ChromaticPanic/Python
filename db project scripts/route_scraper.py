import os
import csv
import sys
import requests
import json
import pandas as pd
import numpy as np
import time

def main():
   inPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\"
   fileName = "stops.csv"
   inFile = inPath + fileName
   outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\"
   outfile = outPath + fileName[:-4] + "_filled.csv"
   
   if not os.path.isfile(inFile):
      input("Press any key to exit")
      sys.exit(1)

   df = pd.read_csv(inFile, keep_default_na=False)
   df_out = pd.DataFrame(index=np.arange(436800), columns=["stop_id","route_id"])

   print(df.to_string())
   searchString = ""
   reqCount = len(df.index)
   outRow = 0

   for i in range( 0, reqCount - 1 ):
   #for i in range( 0, 1 ):

      searchString = df.at[i,'stop_id']

      url = "https://api.winnipegtransit.com/v3/stops/" 
      url += str(searchString)
      url += "/schedule.json?api-key=Q9LAaJ9mfpr4nlLSWzsK"

      payload={}
      headers = {}

      response = requests.request("GET", url, headers=headers, data=payload)
      #stop_id stop_code stop_name stop_lat stop_lon stop_url
      try:
         for j in response.json()['stop-schedule']['route-schedules']:
            df_out.at[outRow, "stop_id"] = df.at[i,'stop_id']
            df_out.at[outRow, "route_id"] = j['route']['key']
            outRow += 1
      except:
         print("Error: " + str(searchString))
         continue
      print("request " + str(i) + "/" + str(reqCount) + " " + str(searchString) + " ...complete")
      time.sleep(1)
   
   df_out.to_csv(outfile, index=False)
   input("Press any key to exit")
   sys.exit(0)



if __name__=="__main__":
   main()