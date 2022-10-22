import os
import csv
import sys
import pandas as pd
import geopandas as gpd
from shapely import wkt

def main():
    inPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    fileName = "4_Parks_and_Open_Space_updatedv2.csv"
    inFile = inPath + fileName
    outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    outfile = outPath + "4_parkTransitv2.csv"

    stopsFile = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\" + "1_stops_updated.csv"
    temp = pd.read_csv(stopsFile)
    temp['geometry'] = temp['geometry'].apply(wkt.loads)
    stops = gpd.GeoDataFrame(temp, crs="EPSG:4326", geometry='geometry')

    if not os.path.isfile(inFile):
        input("Press any key to exit")
        sys.exit(1)
    cols = ['park id', 'stop_id', 'distance']
    temp = pd.read_csv(inFile)
    temp['geometry'] = temp['geometry'].apply(wkt.loads)
    df = gpd.GeoDataFrame(temp, crs="EPSG:4326", geometry='geometry')
    
    stops['geometry'] = stops['geometry'].to_crs('EPSG:26914')
    df['geometry'] = df['geometry'].to_crs('EPSG:26914')

    with open(outfile, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(cols)
        
        for index, row in df.iterrows():
            for index2, row2 in stops.iterrows():
                distance = row['geometry'].distance(row2['geometry'])
                if distance < 400:
                    outrow = [row['park id'], row2['stop_id'], distance]
                    print(outrow)
                    writer.writerow(outrow)
                
    #print(outdf)
    #outdf.to_csv(outfile, index=False)
    #input("Press any key to exit")
    sys.exit(0)


if __name__ == "__main__":
    main()