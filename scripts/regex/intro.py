import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"  # This regular expression matches a string enclosed in square brackets followed by one or more digits
result = re.search(regex, log)  # Search the string log for a match to the regular expression
print(result[1])

# The grep command on the CLI
# grep [text/regex] [flag] pattern [filepath]
# -i: Ignore case distinctions.
# -r: Recursively search directories.
# -v: Invert match, showing lines that do not match the pattern.
# -w: Match whole words only.
# -E: Use extended regular expressions.
# -x: Match whole lines only.

# Advanced matching
# . : Matches any single character except newline characters.  E.g a.b finds a1b, a-b
# ^ : Matches the start of a line.  E.g grep ^hello file.txt (Lines start with hello)
# $ : Matches the end of a line.   E.g grep world$ file.txt  (Lines end with world)
