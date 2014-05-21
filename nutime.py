#The probability of survival is inversely proportional to the angle of arrival.

import os
import time
from stat import *

#returns a list of all the files on the current directory
files = os.listdir('.')

for f in files:
  #my folder has some jpegs and raw images
  if f.lower().endswith('jpg'):
    st = os.stat(f)
    atime = st[ST_ATIME] #access time
    mtime = st[ST_MTIME] #modification time

    new_mtime = mtime + (4*3600) #new modification time

    #modify the file timestamp
    os.utime(f,(atime,new_mtime))
