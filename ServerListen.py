#!/usr/bin/env python
# adpated from example "Hello World!" script at tornadoweb.org
import tornado.ioloop
import tornado.web
from subprocess import call
import os

# Here we have a class called 'On' which will run two commands: date and codesend (date, because I want to see on the RPi terminal when the codesend command was executed)
# the command: "codesent 283955" will send a signal via GPIO to my 433MHz transmitter module, which will turn on my wireless outlet.
class On(tornado.web.RequestHandler):
        def get(self):
                os.system('date; codesend 283955')

		
class Off(tornado.web.RequestHandler):
	def get(self):
		os.system('date; codesend 283964')


class On2(tornado.web.RequestHandler):
        def get(self):
                os.system('date; codesend 284099')

		
class Off2(tornado.web.RequestHandler):
	def get(self):
		os.system('date; codesend 284108')

class On3(tornado.web.RequestHandler):
	def get(self):
		os.system('date; codesend 284419')

class Off3(tornado.web.RequestHandler):
	def get(self):
		os.system('date; codesend 284428')
		
#       Codes for First Remote
#       ON              OFF
#1       283955          283964
#2       284099          284108
#3       284419          284428
#4       285955          285964
#5       292099          292108
# the above 5 lines are the result of using Tim Lelands RFSniffer program.
                
# This here is the list of address/extentions the webserver will react to.
# If I type into a computer (or Tasker:HTTP Get action) "{RPiaddress}:{Port for this server}/on/"   ex: "192.168.1.50:7777/on/"
#	then the class "On" (at line 16) will be executed by the server as a response to the request.
application = tornado.web.Application([
	(r"/on/", On),
	(r"/off/", Off),
        (r"/on2/", On2),
        (r"/off2/", Off2),
        (r"/on3/", On3),
        (r"/off3/", Off3),
])
# Here is where we can define the port the webserver will listen on. Currently set for 7777
if __name__ == "__main__":
	application.listen(7777)
	tornado.ioloop.IOLoop.instance().start()
