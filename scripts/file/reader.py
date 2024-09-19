#!/usr/bin/env python3

# with open("spider.txt") as file: -> Auto close file for you

file = open("testfile.txt")

print(file.readline())

print(file.readline())

# The readline() method reads a single line from the current position, 
# the read() method reads from the current position until the end of the file.

print(file.read())

file.close()
