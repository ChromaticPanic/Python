import os
import csv
import sys
import shutil
import time

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Main
# Check system python version, must be 3.1 or greater
# Ask join type
# Ask for file names
# mode - variable to determine which join to perform
# file1 - first file to join
# file2 - second file to join
def main():

    version = (3, 1)
    if sys.version_info < version:
        print("This script requires Python 3.1 or greater")
        sys.exit(1)

    mode = int(getJoinType())
    print("Enter file names for the two tables to join:")
    print("   File 1:   ")
    file1 = open(getFile(), "r")
    print("   File 2:   ")
    file2 = open(getFile(), "r")

    header1 = getHeader(file1)
    header2 = getHeader(file2)

    pairList = matchColumns(file1, file2, header1, header2)
    outColumnMap, outHeader = mapOutputColumns(header1, header2, pairList)

    if pairList:
        if mode == 1:
            naturalJoin(file1, file2, pairList, outColumnMap, outHeader)
        elif mode == 2:
            leftJoin(file1, file2, pairList, outColumnMap, outHeader)
        elif mode == 3:
            fullOuterJoin(file1, file2, pairList, outColumnMap, outHeader)
        elif mode == 4:
            cartesianJoin(file1, file2, outColumnMap, outHeader)
        elif mode == 5:
            naturalJoin(file1, file2, pairList, outColumnMap, outHeader)
            fullOuterJoin(file1, file2, pairList, outColumnMap, outHeader)
        elif mode == 6:
            naturalJoin(file1, file2, pairList, outColumnMap, outHeader)
            fullOuterJoin(file1, file2, pairList, outColumnMap, outHeader)
            cartesianJoin(file1, file2, header1, header2)
        else:
            sys.exit(1)
    else:
        print("No matching columns found")
        sys.exit(1)

    file1.close()
    file2.close()
    print("Program Completed Successfully")
    input("Press Any Key to exit.")
    sys.exit(0)

# Natural Join
# Combine rows from both files that match on all columns
# pairList - list of matching column pairs as int tuples
# outColumnMap - list of tuples of that map columns from each input file to the output file
def naturalJoin(csvfile1, csvfile2, pairList, outColumnMap, outHeader):

    print("Generating Natural Join --- .csv  ...... ", end="", flush=True)
    outFile = open(dname + "\\Natural_join.csv", "w", newline="")

    writer = csv.writer(outFile, delimiter=',')
    writer.writerow(outHeader)

    # loop through rows in first file and second file
    for row1 in csv.reader(csvfile1, delimiter=','):
        for row2 in csv.reader(csvfile2, delimiter=','):
            paramMatch = 0

            # Check if values match on all columns between the two rows
            for pair in pairList:
                if row1[pair[0]] == row2[pair[1]]:
                    if not row1[pair[0]] == "NULL":
                        paramMatch += 1

            # If data matches on all columns, generate outputrow and write to file
            if paramMatch == len(pairList):
                outRow = []
                for column in outColumnMap:
                    if column[0] == 0:
                        outRow.append(row1[column[1]])
                    else:
                        outRow.append(row2[column[1]])

                writer.writerow(outRow)
        csvfile2.seek(0)
    csvfile1.seek(0)

    print("done")
    outFile.close()
    return

# Left Join
# Show combination of rows from both files that match on all columns listed in pairList
# Columns unique to the 2nd file are filled with NULL values if no rows are found that have matching values in the first file
def leftJoin(csvfile1, csvfile2, pairList, outColumnMap, outHeader):

    print("Generating Left Join --- .csv  ...... ", end="", flush=True)
    outFile = open(dname + "\\Left_join.csv", "w", newline="")

    writer = csv.writer(outFile, delimiter=',')
    writer.writerow(outHeader)

    reader1 = csv.reader(csvfile1, delimiter=',')
    reader2 = csv.reader(csvfile2, delimiter=',')
    next(reader1)

    # loop through rows in first file
    for row1 in reader1:
        rowMatch = 0
        next(reader2)

        # loop through rows in second file
        for row2 in reader2:
            paramMatch = 0

            # Check if values match on all columns between the two rows
            # and check that the value is not the string NULL
            for pair in pairList:
                if row1[pair[0]] == row2[pair[1]]:
                    if not row1[pair[0]] == "NULL":
                        paramMatch += 1

            # If data matches on all columns, generate outputrow and write to file
            if paramMatch == len(pairList):
                outRow = []
                rowMatch += 1
                for column in outColumnMap:
                    if column[0] == 0:
                        outRow.append(row1[column[1]])
                    else:
                        outRow.append(row2[column[1]])

                writer.writerow(outRow)

        # If no rows were found in the second file that match the first file's row,
        # Use the first file's row and fill in the missing columns with NULL values
        outRow = []
        if rowMatch == 0:
            for column in outColumnMap:
                if column[0] == 0:
                    outRow.append(row1[column[1]])
                else:
                    outRow.append("NULL")

            writer.writerow(outRow)
        csvfile2.seek(0)
    csvfile1.seek(0)

    print("done")
    outFile.close()
    return

# Full Outer Join
# Show combination of rows from both files that match on all columns listed in pairList
# If there are no corresponding rows with matching values, missing values are filled with NULL
# Uses Left Join then appends rows from the second file which do not have matching values in the first file
def fullOuterJoin(csvfile1, csvfile2, pairList, outColumnMap, outHeader):

    print("Generating Full Outer Join --- .csv  ...... ", end="", flush=True)

    leftJoin(csvfile1, csvfile2, pairList, outColumnMap, outHeader)

    shutil.copyfile(dname + "\\Left_join.csv", dname + "\\Full_outer_join.csv")
    outFile = open(dname + "\\Full_outer_join.csv", "a", newline="")

    writer = csv.writer(outFile, delimiter=',')

    reader1 = csv.reader(csvfile1, delimiter=',')
    reader2 = csv.reader(csvfile2, delimiter=',')
    next(reader2)

    # loop through rows in second file
    for row2 in reader2:
        rowMatch = 0
        next(reader1)

        # loop through rows in first file
        for row1 in reader1:
            paramMatch = 0

            # Check if values match on all columns between the two rows
            for pair in pairList:
                if row1[pair[0]] == row2[pair[1]]:
                    if not row1[pair[0]] == "NULL":
                        paramMatch += 1
            
            # If data matches on all columns, increment counter
            if paramMatch == len(pairList):
                rowMatch += 1

        # If no rows were found in the first file that match the second file's row,
        # Use the second file's row and fill in the missing columns with NULL values
        outRow = []
        if rowMatch == 0:

            for column in outColumnMap:
                if column[0] == 0:
                    if column[2] > -1:
                        outRow.append(row2[column[2]])
                    else:
                        outRow.append("NULL")
                else:
                    outRow.append(row2[column[1]])

            writer.writerow(outRow)
        csvfile1.seek(0)
    csvfile2.seek(0)

    print("done")
    outFile.close()
    return

# Generate Natural Join/cross product/cartesian product of two files
def cartesianJoin(csvfile1, csvfile2, header1, header2):

    print("Generating Cross Product --- crossproduct.csv  ...... ", end="", flush=True)
    outFile = open(dname + "\\Cross_product.csv", "w", newline="")

    writer = csv.writer(outFile, delimiter=',')
    writer.writerow(header1 + header2)

    reader1 = csv.reader(csvfile1, delimiter=',')
    reader2 = csv.reader(csvfile2, delimiter=',')
    next(reader1)

    for row1 in reader1:
        next(reader2)

        for row2 in reader2:

            writer.writerow(row1 + row2)

        csvfile2.seek(0)

    csvfile1.seek(0)
    print("done")
    outFile.close()
    return

# Return the header of csvfile
def getHeader(csvfile):
    csvread = csv.reader(csvfile, delimiter=',')
    header = next(csvread)
    return header

# Return a list of integer tuple column pairs that have matching headers
def matchColumns(file1, file2, header1, header2):
    index1 = 0
    index2 = 0
    pairList = []
    matchCount = 0

    for col1 in header1:

        for col2 in header2:

            if col1 == col2:
                matchCount = matchCount + 1
                pairList.append([index1, index2])
            index2 = index2 + 1

        index1 += 1
        index2 = 0

    if matchCount == 0:
        print("No columns matched, generating cross product")
        cartesianJoin(file1, file2, header1, header2)
        print("No other joins will be performed")
        input("Press Any Key to exit.")
        sys.exit(0)

    return pairList

# Return a 3 tuple list (0,1,2) where 
# 0 is the file flag (0 = file1, 1 = file2)
# 1 is the column index
# 2 is the column index of the matching column in the other file
# -1 is used for the column index if the column does not have a matching column in the other file
def mapOutputColumns(header1, header2, pairList):
    outColumnMap = []
    outHeader = []
    index1 = 0
    index2 = 0

    for col1 in header1:
        outHeader.append(col1)
        outColumnMap.append([0, index1, -1])
        index1 += 1

    # only map the columns that are not in the left file
    for col2 in header2:
        if col2 not in header1:
            outHeader.append(col2)
            outColumnMap.append([1, index2, -1])
        index2 += 1

    # copy the column index of the matching column in the other file from pairlist to outColumnMap
    for item in outColumnMap:
        if item[0] == 0:
            for pair in pairList:
                if pair[0] == item[1]:
                    item[2] = pair[1]
        else:
            for pair in pairList:
                if pair[1] == item[1]:
                    item[2] = pair[0]

    return outColumnMap, outHeader

# Request user input for the join parameters
def getJoinType():
    print("************  SQL Join Sim  ***********************")
    print("Select join type then provide 2 file names")

    print("A separate csv file will be generated for each join")
    print("   Natural Join  ......................... 1")
    print("      Left Join  ......................... 2")
    print("Full Outer Join  ......................... 3")
    print(" Cross Product   ......................... 4")
    print("Generate Joins 1,2,3  .................... 5")
    print("Generate Joins 1,2,3,4 ................... 6")
    print("   Quit  ................................. 7")
    val = input("Select Join Type:")

    if int(val) < 1 or int(val) > 6:
        print("Invalid choice, only 1,2,3,4,5,6 allowed")
        input("Press Any Key to exit.")
        sys.exit(1)

    return val

# Check if the file exists
def getFile():
    fileName = input()
    if os.path.isfile(fileName):
        return fileName
    else:
        print("File does not exist")
        input("Press Any Key to exit.")
        sys.exit(1)


if __name__ == "__main__":
    main()
