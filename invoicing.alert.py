#!/usr/bin/env python

from win32com.client import Dispatch
import datetime, time
import re
import smtplib

session = Dispatch("MAPI.session")
session.Logon('OUTLOOK')  # MAPI profile name
inbox = session.Inbox

inv = None
invok = 0

for i in range(inbox.Messages.Count):
    message = inbox.Messages.Item(i + 1)
    d1 = "%s" % message.TimeReceived
    d2 = datetime.datetime.strptime(d1, "%m/%d/%y %H:%M:%S")
    n1 = datetime.datetime.today() - d2

    print d1, d2, n1.days
    if message.Subject == 'REAL RECORDS : UK TNT Invoice Reconcilliation Records...': 
        if n1.days == 0:
            text = message.Text[472:-27]
            rows = text.split('\n')
            inv = 1
            for row in rows:
                fields = [f for f in row.split(' ') if f != u'' ]
                inv = re.search('^ZSD_GB_INVOICES_E_GB10_.*', fields[1])
                if inv and fields[2] == fields[3]:
                    print fields[2], fields[3]
                    invok = 1
                else:
                    print fields
        

me = 'farringtonni@grouphc.net'
header = 'To:%s \nFrom: %s\n' % (me, me) 
if inv and invok:
    header += 'Subject:Invoicing Routine SUCCESS \n'
    msg = header + '\n The totals from this SQL output matches \n\n'
else:
    if inv:
        header += 'Subject:Invoicing Routine FAIL \n'
        msg = header + '\n There has been a mismatch in the Biztalk email \n\n'
    else:
        header += 'Subject:Invoicing Routine FAIL \n'
        msg = header + '\n There was no email confirmation from Biztalk \n\n'

try:
    server = smtplib.SMTP('GBRNonAuthSMTP1.grouphc.net') 
except:
    pass

print 'send message %s' % msg
server.sendmail(me, me, msg )
server.quit()

session.Logoff()    
