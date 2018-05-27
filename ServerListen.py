#!/usr/bin/env python
# adpated from example "Hello World!" script at tornadoweb.org
import tornado.ioloop
import tornado.web
from subprocess import call
import os


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
                

application = tornado.web.Application([
	(r"/on/", On),
	(r"/off/", Off),
        (r"/on2/", On2),
        (r"/off2/", Off2),
        (r"/on3/", On3),
        (r"/off3/", Off3),
])
if __name__ == "__main__":
	application.listen(7777)
	tornado.ioloop.IOLoop.instance().start()
