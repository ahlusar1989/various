""" oneperfile.py - mss sql server used to be able to generate a script file for each object.
someone at Redmond thought it wasn't a good idea to allow us to continue doing that

This script takes the one big file output from SSMS and makes a lot of little files named
after the object they create.

Author:  Niall <hollerith@gmail.com>
Date:    4 May 2010
"""

import re
import sys

def main():

    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        # Test
        name = 'sps.sql'

    src = open(name, "r")
    lines = src.readlines()
    src.close()
    
    pattern = re.compile(r'.*StoredProcedure \[dbo\]\.\[(.*)\].*Script Date.*')

    txt = None
    for line in lines:
        print line
        result = pattern.search(line)
        if result:
            if txt: txt.close()
            name = '%s.sql' % result.group(1)
            txt = open(name, "w")
            txt.write(line)
        else:
            if txt: txt.write(line)

    txt.close()            
    return

if __name__ == "__main__":
    main()
