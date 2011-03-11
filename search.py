""" search.py - search a file using regex

Author:  Niall <hollerith@gmail.com>
Date:    7 Jun 2006
"""

import re
import os
import sys
import time

def main():

    if len(sys.argv) > 0:
        path = sys.argv[1]
    else:
        return ""

    rawstr = r"""<UFORM:ULABEL>(.*)</UFORM:ULABEL>.*<UFORM:UTRANSACT>(\d)</UFORM:UTRANSACT>"""
    uobjtype = re.compile(rawstr, re.IGNORECASE| re.MULTILINE| re.DOTALL)

    File = file(path)
    src = File.read()
    File.close()

    result = uobjtype.search(src)
    if result:
        if (result.group(2) == "0"):
            print result.group(1)

    return(result.group(1))

if __name__ == "__main__":
    main()