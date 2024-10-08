#!/usr/bin/env python3

import os

def parent_directory():
    # Create a relative path to the parent
    # of the current working directory
    relative_parent = os.path.join(os.getcwd(), os.pardir)

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)

print(parent_directory())

