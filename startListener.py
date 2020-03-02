#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author 7hgTnec
# This file is a remote start server
# it will listen on 59782 port
# and if it detected a file name is "start" on current directory
# then this program will send an signal to ESP8266 NodeMCU to let it start the PC
import socket
import os
import time


if __name__ == "__main__":
    print("Sever start.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 59782))
    sock.listen(5)
    msg = ""
    print("Start listening port 59782...")
    while True:
        connection, address = sock.accept()
        connection.settimeout(10)
        val = 0
        print('get connection ' + time.strftime("%Y-%m-%d %H:%M:%S %z", time.localtime(time.time())))
        while True:
            val += 1
            if val == 10:
                msg = b'3'
                connection.send(msg)
                val = 0
                try:
                    data = connection.recv(10)
                except socket.timeout:
                    if os.path.isfile("start"):
                        os.remove("start")

            if os.path.isfile("start"):
                msg = b'1'
                connection.send(msg)
                os.remove("start")
                connection.recv(10)

            time.sleep(0.1)
        connection.close()
        print("Disconnect" + time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(time.time())))


