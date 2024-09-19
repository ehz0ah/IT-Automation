#!/usr/bin/env python3
with open("testfile.txt") as file:
    for line in file:
        print(line.strip().upper()) # strip to remove the new line, see lines.py
