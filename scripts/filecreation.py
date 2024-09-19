#!/usr/bin/env python3

import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass  # This creates an empty file

    # Get the timestamp of when the file was modified
    timestamp = os.path.getmtime(filename)

    # Convert the timestamp into a readable format (datetime object)
    modified_time = datetime.datetime.fromtimestamp(timestamp)

    # Return just the date portion in the format yyyy-mm-dd
    return modified_time.strftime("%Y-%m-%d")

print(file_date("newfile.txt"))
# Should print today's date in the format yyyy-mm-dd

