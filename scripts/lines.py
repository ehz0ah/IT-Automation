#!/usr/bin/env python3
file = open("testfile.txt")
lines = file.readlines() # Read ALL lines
file.close()
lines.sort()
print(lines)
