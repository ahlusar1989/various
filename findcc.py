""" findcc.py - detect data protection issues

Author:  Niall <hollerith@gmail.com>
Date:    7 Oct 2005
"""

import re
import os
import sys
import time

def ValidateLuhnChecksum(number_as_string):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(number_as_string)
    oddeven = num_digits & 1

    for i in range(0, num_digits):
        digit = int(number_as_string[i])

        if not (( i & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit
        
    return ( (sum % 10) == 0 )

def main():

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        # Test
        path = 'C:\\'

    # All files called .XML in this folder
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                #if name.endswith('.XML'):
                process(os.path.join(root, name))
    else:
        # Just this file
        process(path)

def process(name):
    
    visa = re.compile(r'^4([0-9]{12,15})$')
    mastercard = re.compile(r'^5[12345]([0-9]{14})$')
    
    try:    
        src = open(name, "r")
        lines = src.readlines()
        src.close()

        for line in lines:
            result = visa.search(line)
            if result:
                print 'Visa', result.group(0)
    
            result = mastercard.search(line)
            if result:
                print 'Mastercard', result.group(0)                
    except:
        print 'Cannot open file %s' % name
       
    return

if __name__ == "__main__":
    main()
