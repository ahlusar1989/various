"""
Where's Wally (or waldo if you speak 'american')

Usage:

python wally.py <username>

"""
import os, sys

try:
  wally = sys.argv[1]
except:
  wally = 'ntusername'

#servers = os.popen('query termserver').read()
#servers = servers.split('\n')
#servers = servers[2:]

servers = open('network.txt').read().split('\n')

for server in servers:
  result = os.popen('query user %s /server:%s' % (wally, server)).read()
  if result: 
    print server
    print result

print '-30-'
