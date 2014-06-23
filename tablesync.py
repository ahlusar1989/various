"""
    tablesync.py
    Niall Farrington March 2011

    This is not a generic tool

    This script is for use with the tablediff script
    It is used to finish replication

    TODO: Merge the two scripts to use worker threads

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 

"""
import sys, os, subprocess
import adodbapi
import glob

# import constants from a relative path
TARGETDIR = os.getcwd()
sys.path.append(TARGETDIR)

try:
    from settings import *
except ImportError:
    TARGETSERVER = 'GBRSDHEID0004'
    TARGETDB = 'farringtonni'

CONNECTION_STRING = "PROVIDER=SQLOLEDB;DATA SOURCE=%s;DATABASE=%s;Integrated Security=SSPI" % (TARGETSERVER, TARGETDB)

print adodbapi.version # show version
if TARGETSERVER == 'GBRSDHEID0001': sys.exit()
    
connection = adodbapi.connect(CONNECTION_STRING)
c = connection.cursor()

os.chdir(TARGETDIR)
for name in glob.glob('*.sql'):

    filepath = os.path.join(TARGETDIR, name)
    print 'Processing %s...' % filepath
    try:
        f = open(filepath, 'r')
        line, lines = f.readline(), []
        while line:
            if len(lines)==BATCH_SIZE:
                print ''.join(lines)
                c.execute(''.join(lines))
                connection.commit()
                lines = []
            else:
                if not line.startswith('--'): lines += [line]
            line = f.readline()
        if lines:
            print ''.join(lines)
            c.execute(''.join(lines))
            connection.commit()
        f.close()
        os.remove(filepath)
        print 'Removed %s' % filepath
    except adodbapi.DatabaseError,  inst:
        print "Database error", inst.args[0]    # should be the error message
    except:
        print "Unexpected error:", sys.exc_info()[0]

c.close()
connection.close()

