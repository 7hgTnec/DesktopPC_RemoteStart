#!/bin/bash
# Author 7hgTnec
# This file is a remote start server
# it will listen on 59782 port
# and if it detected a file name is "start" on current directory
# then this program will send an signal to ESP8266 NodeMCU to let it start the PC

if __name__ == "__main__":
    import socket
    import os
    import time
    print("Sever start.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('your server IP', 59782))
    sock.listen(5)
    msg = ""
    print("Start listening port 59782...")
    while True:
        connection,address = sock.accept()
        timeoutFlag = False
        val = 0
        print('get connection'+ time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())))
        while True:
            val += 1
            if(val == 1000000):
		msg = b'3'
                connection.send(msg)
                val = 0
                try:
                    connection.settimeout(1)
                    data = connection.recv(10)
                except socket.timeout:
                    timeoutFlag = True
            if timeoutFlag == True:
		try:
		  os.system("rm -f start")
		except IOError as err:
		  pass
                break
            try:
                startFlag = open('./start','r')
		msg = b'1'
                connection.send(msg)
                startFlag.close()
                os.system("rm -f start")
		connection.recv(10)
		print("Be started at " + time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())))
            except IOError as err:
                pass
        connection.close()
        print("Disconnect" + time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())))


