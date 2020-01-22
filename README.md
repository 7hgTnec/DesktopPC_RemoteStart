# DesktopPC_RemoteStart
The depend library comes from https://github.com/esp8266/Arduino.git

Basic idear is use iPhone shorcut to run an ssh command and creat an file name is start

Then while the startListener.py detected this file it will send an signal to NodeMCU model

When NodeMCU model receive that signal will pu relay close to short the powerSW+-

Also the wire from case's switch can connect with the wire from relay in parallel

And then connect with powerSW on motherboard such that the case's switch can still work.

![image](https://github.com/7hgTnec/DesktopPC_RemoteStart/edit/master/Connection.jpg)
