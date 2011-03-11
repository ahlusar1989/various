""" xustamp.py - strip timestamp values from uniface xml

Author:  Niall <hollerith@gmail.com>
Date:    7 Oct 2005
"""

import re
import os
import sys
import time

def main():

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        # Test
        path = 'C:\\Program Files\\Compuware\\Uniface 9.3.01\\project\\trunk'

    # All files called .XML in this folder
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                #if name.endswith('.XML'):
                striptimestamp(os.path.join(root, name))
                stripcompstamp(os.path.join(root, name))
    else:
        # Just this file
        striptimestamp(path)
        stripcompstamp(path)

def striptimestamp(name):

    pattern = re.compile(r'<DAT name="UTIMESTAMP">(.*)</DAT>')

    src = open(name, "r")
    lines = src.readlines()
    src.close()

    src = open(name, "w")
    for line in lines:
        result = pattern.search(line)
        if result:
            src.write('<DAT name="UTIMESTAMP"></DAT>\n')
        else:
            src.write(line)
    return

def stripcompstamp(name):

    pattern = re.compile(r'<DAT name="UCOMPSTAMP">(.*)</DAT>')

    src = open(name, "r")
    lines = src.readlines()
    src.close()

    src = open(name, "w")
    for line in lines:
        result = pattern.search(line)
        if result:
            src.write('<DAT name="UCOMPSTAMP"></DAT>\n')
        else:
            src.write(line)
    return

if __name__ == "__main__":
    main()
