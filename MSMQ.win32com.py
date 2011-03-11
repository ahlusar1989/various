###########################################
## Microsoft Messaging Queue (MSMQ) Examples
###########################################

############################################
## Example #1: Write to a private Queue
############################################

import win32com.client
import time

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
qinfo.FormatName="direct=os:tera\\PRIVATE$\\Hello"  

queue=qinfo.Open(2,0)   # Open a ref to queue

msg=win32com.client.Dispatch("MSMQ.MSMQMessage")

for i in xrange(100):
	msg.Label="Test #" + str(i)
	msg.Body = "This is test time #" + str(i) + "  Time:" + time.ctime(time.time() )
	msg.Send(queue)

queue.Close()




############################################
## Example #2: Read a Message Blocked version
############################################

import win32com.client
import time

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
qinfo.FormatName="direct=os:tera\\PRIVATE$\\Hello"  

queue=qinfo.Open(1,0)   # Open a ref to queue to read(1)

msg=queue.Receive()
print "Label",msg.Label
print "Body",msg.Body

queue.Close()




##################################################
## Example #3: Process All Messages
##################################################

import win32com.client
import time

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
qinfo.FormatName="direct=os:tera\\PRIVATE$\\Hello"  

queue=qinfo.Open(1,0)   # Open a ref to queue to read(1)

while 1:
	msg=queue.Receive()
	print "Label:",msg.Label
	print "Body :",msg.Body

queue.Close()



##################################################
## Example #4: Peek a Message without removing it
##################################################

import win32com.client
import time

qinfo=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
qinfo.PathName=".\\PRIVATE$\\HelloWorld"  # Private Queue on local machine

queue=qinfo.Open(1,0)   # Open a ref to queue to read(1)

msg=queue.Peek()
print "Label",msg.Label
print "Body",msg.Body

queue.Close()



