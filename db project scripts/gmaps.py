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
   fileName = "address.csv"
   inFile = inPath + fileName
   outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\"
   outfile = outPath + fileName[:-4] + "_filled.csv"
   
   if not os.path.isfile(inFile):
      input("Press any key to exit")
      sys.exit(1)

   df = pd.read_csv(inFile, keep_default_na=False)

   print(df.to_string())
   searchString = ""
   reqCount = len(df.index)
   for i in range( 0, reqCount ):
   #for i in range( 0, 1 ):
      if df.at[i,'Address'] == "":

         searchString = df.at[i,'Name']
         searchString = searchString.replace("-", "+")
         searchString = searchString.replace(" ", "+")

         url = "https://maps.googleapis.com/maps/api/directions/json?origin=Winnipeg&destination=" 
         url += searchString + "+winnipeg"
         url += "&mode=walking&key=AIzaSyBSQGLUtm0eifJQPJoIGcxICXFiqu0yVe4"

         payload={}
         headers = {}

         response = requests.request("GET", url, headers=headers, data=payload)

         try:
            if response.json()['routes'][0]['legs'][0]['end_address'] == "Winnipeg, MB, Canada":
               df.at[i,'Address'] = "Not Available"
               df.at[i,'Lat'] = ""
               df.at[i,'Long'] = ""
            else:
               df.at[i,'Address'] = response.json()['routes'][0]['legs'][0]['end_address']
               df.at[i,'Lat'] = response.json()['routes'][0]['legs'][0]['end_location']['lat']
               df.at[i,'Long'] = response.json()['routes'][0]['legs'][0]['end_location']['lng']
         except:
            print("Error: " + searchString)
            df.at[i,'Address'] = "Not Available"
            df.at[i,'Lat'] = ""
            df.at[i,'Long'] = ""
            continue
         print("request " + str(i) + "/" + str(reqCount) + " " + searchString + " ...complete")
         time.sleep(0.300)
         
      if df.at[i,'Address'] == "Winnipeg, MB, Canada":
         df.at[i,'Address'] = "Not Available"
         df.at[i,'Lat'] = ""
         df.at[i,'Long'] = ""
   
   df.to_csv(outfile, index=False)
   input("Press any key to exit")
   sys.exit(0)



if __name__=="__main__":
   main()