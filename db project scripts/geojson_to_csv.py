import os
import csv
import sys
import json
import fiona
import pandas as pd
import geopandas as gpd
from shapely import wkt


def main():
    inPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\RawTables\\"
    fileName = "Provincial Electoral District boundary.csv"
    inFile = inPath + fileName
    # inFile = inPath + "Census 2006 - Neighbourhood Boundary.geojson"
    # geoFile_ward = inPath + "Census 2006 - Electoral Ward Boundary.geojson"
    # geoFile_school = inPath + "School Division.geojson"
    # geoFile_province = inPath + "2018_prov.geojson"
    geoFile_province = inPath + "2018_prov.zip"

    outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\"
    # outfile = outPath + fileName[:-8] + "_geojson.csv"
    outfile = outPath + fileName[:-4] + "_geojson.csv"

    if not os.path.isfile(inFile):
        input("Press any key to exit")
        sys.exit(1)

    gdf = gpd.read_file(inPath + "2018_prov.zip")
    gdf = gdf.to_crs("EPSG:4326")
    #print(gdf)
    #gdf = gpd.read_file(inFile)
    gdf.rename(columns = {'ED':'name'}, inplace = True)
    gdf.drop(columns = ['ED_French','Type','SHAPE_Leng', 'SHAPE_Area'], inplace = True)
    gdf['name'] = gdf['name'].str.strip()
    gdf['name'] = gdf['name'].str.replace('[^a-zA-Z]', ' ', regex = True).str.lower()
    gdf['name'] = gdf['name'].str.replace('\s+', ' ', regex = True)
    print(gdf)


    gdf.to_csv(outfile, index=False)

    input("Press any key to exit")
    sys.exit(0)


if __name__ == "__main__":
    main()
