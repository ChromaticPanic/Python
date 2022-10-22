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
    fileName = "1_stops_updated.csv"
    inFile = inPath + "Final\\" + fileName
    geoFile_hood = inPath + "Final\\" + "16_Census 2006 - Neighbourhood Boundary_geojson.csv"
    geoFile_ward = inPath + "Final\\" + "15_Census 2006 - Electoral Ward Boundary_geojson.csv"
    geoFile_school = inPath + "Final\\" + "8_School Division_geojson.csv"
    geoFile_province = inPath + "Final\\" + "17_Provincial Electoral District boundary_geojson.csv"

    outPath = "F:\\Uni Files\\3380\\Project_3380\\Backend\\"
    outfile = outPath + fileName[:-4] + ".csv"

    if not os.path.isfile(inFile):
        input("Press any key to exit")
        sys.exit(1)

    points = pd.read_csv(inFile, keep_default_na=False)
    points['geometry'] = points['geometry'].apply(wkt.loads)
    gdf = gpd.GeoDataFrame(points, crs="EPSG:4326")

    hood = pd.read_csv(geoFile_hood, keep_default_na=False)
    hood['geometry'] = hood['geometry'].apply(wkt.loads)
    geo_hood = gpd.GeoDataFrame(hood, crs="EPSG:4326")

    ward = pd.read_csv(geoFile_ward, keep_default_na=False)
    ward['geometry'] = ward['geometry'].apply(wkt.loads)
    geo_ward = gpd.GeoDataFrame(ward, crs="EPSG:4326")

    school = pd.read_csv(geoFile_school, keep_default_na=False)
    school['geometry'] = school['geometry'].apply(wkt.loads)
    geo_school = gpd.GeoDataFrame(school, crs="EPSG:4326")

    province = pd.read_csv(geoFile_province, keep_default_na=False)
    province['geometry'] = province['geometry'].apply(wkt.loads)
    geo_province = gpd.GeoDataFrame(province, crs="EPSG:4326")

    # gdf.rename(columns={'Last': 'name'}, inplace=True)
    # #gdf.drop(columns=['ED_French', 'Type', 'SHAPE_Leng', 'SHAPE_Area'], inplace=True)
    # gdf['name'] = gdf['name'].str.strip()
    # gdf['name'] = gdf['name'].str.replace('[^a-zA-Z]', ' ', regex=True).str.lower()
    # gdf['name'] = gdf['name'].str.replace('\s+', ' ', regex=True)
    #print(gdf)

    # df_out1 = gpd.sjoin(gdf, geo_hood, how='left', op='within').drop(['index_right'], axis=1).rename(columns={'name_left': 'name', 'name_right': 'neighbourhood', 'number': 'neighbourhood_id'})
    # df_out2 = gpd.sjoin(df_out1, geo_ward, how='left', op='within').drop(['index_right', 'census_year'], axis=1).rename(columns={'name_left': 'name','name_right': 'ward'})
    # df_out3 = gpd.sjoin(df_out2, geo_school, how='left', op='within').drop(['index_right', 'website'], axis=1).rename(columns={'name_left': 'name', 'division': 'school_div_id', 'name_right': 'school_div'})
    # df_out4 = gpd.sjoin(df_out3, geo_province, how='left', op='within').drop(['index_right', 'Area', 'OBJECTID'], axis=1).rename(columns={'name_left': 'name','name_right': 'district'})

    geo_hood2 = geo_hood
    geo_hood2['geometry'] = geo_hood['geometry'].to_crs('EPSG:26914').centroid
    geo_ward['geometry'] = geo_ward['geometry'].to_crs('EPSG:26914').buffer(0)
    geo_school['geometry'] = geo_school['geometry'].to_crs('EPSG:26914').buffer(0)
    geo_province['geometry'] = geo_province['geometry'].to_crs('EPSG:26914').buffer(0)

    df_out1 = gpd.sjoin(geo_hood2, geo_ward, how='left', op='intersects').drop(['index_right','census_year'], axis=1).rename(columns={'name_left': 'neighbourhood', 'name_right': 'ward', 'number': 'neighbourhood_id'})
    df_out2 = gpd.sjoin(df_out1, geo_school, how='left', op='intersects').drop(['index_right', 'website'], axis=1).rename(columns={'name_left': 'neighbourhood', 'division': 'school_div_id', 'name': 'school_div'})
    df_out3 = gpd.sjoin(df_out2, geo_province, how='left', op='intersects').drop(['index_right', 'Area', 'OBJECTID'], axis=1).rename(columns={'name_left': 'neighbourhood', 'name': 'district'})
    df_out3['geometry'] = geo_hood['geometry'].to_crs('EPSG:4326')
    # df_out4.rename(columns={'name': 'Last'}, inplace=True)
    #df_out3.drop(columns=['geometry'], inplace=True)
    print(df_out3['ward'].isna().sum())
    print(df_out3['school_div'].isna().sum())
    print(df_out3['district'].isna().sum())
    print(df_out3)
    #df_out4.to_csv(outfile, index=False)
    df_out3.to_csv(outPath + "hood_ward_sch_dist.csv", index=False)

    #input("Press any key to exit")
    sys.exit(0)


if __name__ == "__main__":
    main()
