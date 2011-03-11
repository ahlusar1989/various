import smtplib
 
to = ''
user = ''
pass = ''
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
#smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(user, pass)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print header
msg = header + '\n this is test msg from mkyong.com \n\n'
smtpserver.sendmail(user, to, msg)
print 'done!'
smtpserver.close()
