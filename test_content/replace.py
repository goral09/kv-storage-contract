#!/usr/bin/python

help_str="""
Invalid arguments.

First argument: file in which there's a $CONTENT placeholder that we wish to replace.
Second argument: file whose content we want to replace $CONTENT with.
Third argument: target file where we will write contents of the first file with $CONTENT replaced.
"""

import sys

if len(sys.argv) != 4:
    print help_str
    exit()

source_file_name=str(sys.argv[1])
source_file=open(source_file_name, "rt")
source_content=source_file.read()
source_file.close()

value_file_name=str(sys.argv[2])
value_file=open(value_file_name, "rt")
value_content=value_file.read()
value_file.close()

target_file_name=str(sys.argv[3])

source_content = source_content.replace('$CONTENT', value_content)
target_file=open(target_file_name, "wt")
target_file.write(source_content)
target_file.close()
