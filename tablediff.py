"""
    tablediff.py 
    Niall Farrington March 2011

    This is not a generic tool
    
    This script is for use with the SQL Server tool tablediff.exe
    Checks if tables have changed (probably should use operational stats instead)
    Threads the calls to subprocess of tablediff
    Another script is used to finish replication
    
                                                                              
 Licensed under the Apache License, Version 2.0 (the "License");          
 you may not use this file except in compliance with the License.         
 You may obtain a copy of the License at                                  
                                                                          
     http://www.apache.org/licenses/LICENSE-2.0                           
                                                                          
 Unless required by applicable law or agreed to in writing, software      
 distributed under the License is distributed on an "AS IS" BASIS,        
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
 See the License for the specific language governing permissions and      
 limitations under the License.                                           
                                                                           
  -t 240
  -sourceserver GBRSDHEID0001
  -sourcedatabase COIS
  -sourcetable <tablename>
  -destinationserver GBRSDHEID0004
  -destinationdatabase farringtonni
  -destinationtable <tablename>
  -f C:\data\<tablename>.sql
    
"""
import sys, os, subprocess
import adodbapi

# import constants from a relative path
TARGETDIR = os.getcwd()
sys.path.append(TARGETDIR)

TIMEOUT = 120

try:
    from settings import *
except ImportError:
    print 'Using defaults'
    SOURCESERVER = 'GBRSDHEID0001'
    SOURCEDB = 'COIS'
    TARGETSERVER = 'GBRSDHEID0004'
    TARGETDB = 'farringtonni'
    INTERVAL = 24
    BLACKLIST = "('LOAD_DIPS_Master_Site_Trips', 'tblitemstatus', 'tblorderscats', 'reb_statistics_fil_2', 'reb_statistics_detail_2', 'journeysNCATS', 'SSISConfigurations', 'tblAudit', 'tblAllFiles', 'tblAllFilesGPS', 'tblAllFilesInc', 'TEMP_DATES', 'TEMP_GPS', 'mjc2_params', 'stats_records', 'tblgpsraw2', 'ticket_nos', 'weigh', 'tblDPRsearch', 'tblauditdetail', 'tblauditheader')"
    
BLACKLIST = BLACKLIST or "('none')"
CONNECTION_STRING = "PROVIDER=SQLOLEDB;DATA SOURCE=%s;DATABASE=%s;Integrated Security=SSPI" % (SOURCESERVER, SOURCEDB)
connection = adodbapi.connect(CONNECTION_STRING)
c = connection.cursor()

sql = """

declare @sourceserver varchar(32)
declare @sourcedb varchar(32)
declare @targetserver varchar(32)
declare @targetdb varchar(32)
declare @targetdir varchar(256)

select @sourceserver = '%s', @sourcedb = '%s', @targetserver = '%s', @targetdb = '%s', @targetdir = '%s'

select
	' -sourceserver "'+@sourceserver+'" -sourcedatabase "'+@sourcedb+'" -sourcetable "'+substring(t.name, 1, 32)+'" -destinationserver "'+@targetserver+'" -destinationdatabase "'+@targetdb+'" -destinationtable "'+substring(t.name, 1, 32)+'" -f "'+@targetdir+'\\'+substring(t.name, 1, 32)+'.sql"' as command
 from
	sys.dm_db_index_usage_stats i JOIN
	sys.tables t ON (t.object_id = i.object_id)
where
	database_id = db_id() and last_user_update > dateadd(hour, -%d, getdate()) and
    t.name not in %s
group by t.name
""" % (SOURCESERVER, SOURCEDB, TARGETSERVER, TARGETDB, TARGETDIR, INTERVAL, BLACKLIST)

print sql 

c.execute(sql)
db = c.fetchall()
for rec in db:
    for args in rec:
        tablediff = 'C:\\Program Files\\Microsoft SQL Server\\90\\COM\\tablediff.exe -t %s %s ' % (TIMEOUT, args)
        subprocess.Popen(tablediff) # NOWAIT
        print args

c.close()
connection.close()
