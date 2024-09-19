#!/usr/bin/env python3
# modes: r, w, x, a, r+, in w mode, old contents get deleted once the file is open
with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")
