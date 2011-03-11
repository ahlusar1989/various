import os, subprocess
import adodbapi

# constants
LOGIN, SECRET = 'sapadmin', 'S4p4dmin',
SOURCESERVER = 'GBRSDHEID0001'
SOURCEDB = 'COIS'
TARGETSERVER = 'GBRCL18964'
TARGETDB = 'farringtonni'
TARGETDIR = 'c:\\temp\\'

CSTR = "PROVIDER=SQLOLEDB;DATA SOURCE=%s;UID=%s;PWD=%s;DATABASE=%s"
CONNECTION_STRING = CSTR % (SOURCESERVER, LOGIN, SECRET, SOURCEDB)

def with_connection(func):
    def _exec(*args, **argd):
        conn = adodbapi.connect(CONNECTION_STRING)
        try:
             func(conn, *args, **argd)
        finally:
             conn.close
    return _exec

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
	' -sourceserver "'+@sourceserver+'" -sourcedatabase "'+@sourcedb+'" -sourcetable "'+substring(t.name, 1, 32)+'" -destinationserver "'+@targetserver+'" -destinationdatabase "'+@targetdb+'" -destinationtable "'+substring(t.name, 1, 32)+'" -f "'+@targetdir+substring(t.name, 1, 32)+'.sql"' as command
 from
	sys.dm_db_index_usage_stats i JOIN
	sys.tables t ON (t.object_id = i.object_id)
where
	database_id = db_id() and last_user_update > dateadd(minute, -10, getdate()) and
    t.name in (select u_glab from gbrsdheid0001.uniface.dbo.ucgroup where u_vlab = 'COPS' and u_indb = 'Y') and
	t.name not in ('tblauditheader', 'tblauditdetail')
group by t.name

""" % (SOURCESERVER, SOURCEDB, TARGETSERVER, TARGETDB, TARGETDIR)

#print sql && sqlcmd -b -S'+@targetserver+' -d'+@targetdb+' -i "'+@targetdir+substring(t.name, 1, 32)+'.sql" 

c.execute(sql)
db = c.fetchall()
for rec in db:
    for args in rec:
        subprocess.Popen('C:\\Program Files\\Microsoft SQL Server\\90\\COM\\tablediff.exe ' + args) # NOWAIT

c.close()
connection.close()