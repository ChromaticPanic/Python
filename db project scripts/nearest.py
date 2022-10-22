import os
import csv
import sys
import pandas as pd
import geopandas as gpd
from shapely import wkt

def main():
    inPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    fileName = "6_Tree_Inventory2_updated.csv"
    inFile = inPath + fileName
    outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\"
    outfile = outPath + "treeparkv2.csv"

    stopsFile = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\Final\\" + "4_Parks_and_Open_Space_updatedv2.csv"
    # temp = pd.read_csv(stopsFile)
    # temp['geometry'] = temp['geometry'].apply(wkt.loads)
    # parks = gpd.GeoDataFrame(temp, crs="EPSG:4326", geometry='geometry')
    parks = pd.read_csv(stopsFile)

    if not os.path.isfile(inFile):
        input("Press any key to exit")
        sys.exit(1)
    
    # temp = pd.read_csv(inFile)
    # temp['geometry'] = temp['geometry'].apply(wkt.loads)
    # df = gpd.GeoDataFrame(temp, crs="EPSG:4326", geometry='geometry')
    df = pd.read_csv(inFile)
    
    # parks['geometry'] = parks['geometry'].to_crs('EPSG:26914')
    # df['geometry'] = df['geometry'].to_crs('EPSG:26914')

    outdf = pd.merge(df, parks, how='left', left_on='Park', right_on='park name')
    #outdf.to_csv(outfile)
    #outdf = gpd.sjoin_nearest(df, parks, how="left", max_distance=400)
    #outdf = df.sjoin_nearest(parks, how='left')
    
    #outdf.drop(columns=['location description','total area in hectares','water area in hectares','land area in hectares','ward','ward_id', 'neighbourhood_id','school_div_id','school_div','district'], inplace=True)
    outdf.drop(columns=['location description','total area in hectares','water area in hectares','land area in hectares'], inplace=True)
    print(outdf.head())
    outdf.drop_duplicates(inplace=True, keep='first', subset=['loc_id_x'])
    outdf.to_csv(outfile, index=False)
    sys.exit(0)


if __name__ == "__main__":
    main()