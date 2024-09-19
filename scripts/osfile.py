#!/usr/bin/env python3

import os
import datetime

# os.remove("nonexistentfile.txt")  # throw error
os.rename("emo.txt","novel.txt")

print(os.path.exists("novel.txt"))
print(os.path.exists("emo.txt"))

#This code will provide the file size
print(os.path.getsize("testfile.txt"))

#This code will provide a unix timestamp for the file
print(os.path.getmtime("testfile.txt"))

#This code will provide the date and time for the file in an 
#easy-to-understand format
timestamp = os.path.getmtime("testfile.txt")
print(datetime.datetime.fromtimestamp(timestamp))

#This code takes the file name and turns it into an absolute path
print(os.path.abspath("testfile.txt"))

