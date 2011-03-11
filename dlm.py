""" 
::: Niall Farrington Hanson GBR Cementitious faciebat est. 
::: Cycle through user directories on the citrix boxen removing DLM config directories
"""

import shutil, os, re

hostnames = ['grpstheid0045','grpstheid0044','grpstheid0043','grpstheid0042','grpstheid0041','grpstheid0040',]

def main():

    for host in hostnames:
        path = '\\\\%s\\c$\\documents and settings\\' % host           
        for folder in os.listdir(path):
            dirpath = '%s%s\\.compuware' % (path, folder) 
            try:
                filepath = '%s\\config.xml' % dirpath
                try:
                    f = open(filepath).read()
                    match = re.search('.*license-apr2010.*', f)
                    if match:
                        print 'Removing %s' % dirpath
                        shutil.rmtree(dirpath)
                except IOError:
                    pass
            except WindowsError:
                print 'Directory %s does not exist' % dirpath
                
if __name__ == "__main__":
    main()
