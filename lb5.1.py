filename = "group.txt"
import csv
import glob 
import sys
import os

print ("Select an action: \n1. Read the file \n2. Add new content \n3. search for files in the directory \n4. search for data in a file")
choise = input()
if choise == "1":
    fd = open (filename, "r")
    reader = csv.reader(fd, delimiter="\t")
    for row in reader:
        print (row)

elif choise == "2":
    fd = open (filename, "a+")
    dani = input("Enter the data you want to add: ")
    fd.write(dani + "\n")

elif choise == "3":
    maskafile = input("Enter a file name: ")
    for filename in glob.glob(maskafile):
        print(filename)

elif choise == "4":
    poshuk = input ("Enter the data you want to find: ")

    filedata = open(filename, "r").readlines()
        
    for row in filedata:
        if poshuk in row:
            print(row)