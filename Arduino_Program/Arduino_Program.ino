// Atuhor 7hgTnec
// This is an arduino file running on ESP8266 NodeMCU V1.0
// Dependent libarary comes from 
// https://github.com/esp8266/Arduino.git

#include <ESP8266WiFi.h>
 
const char *ssid     = "Your_WIFI_SSID";
const char *password = "password";
const char *host = "IPAddressOfLocalServer";
const char myRelayCtl = 5; // D1, used to control the relay
WiFiClient client;
const int tcpPort = 59782; // this is a random pick port but have to be same as startListener
 
 
void setup()
{
    //Serial.begin(115200);    
    pinMode(16,OUTPUT);//LED D16, heartbeat light. Will flash onec around every 5 seconds while connected
    pinMode(myRelayCtl,OUTPUT); //D1 start relay
    delay(10);
    WiFi.mode(WIFI_STA);
 
    WiFi.begin(ssid, password);
 
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        //Serial.print(".");
    }
    digitalWrite(myRelayCtl,LOW);
}
 

void loop() {
  // put your main code here, to run repeatedly:
  while(!client.connected()){
    if(!client.connect(host,tcpPort)){
      //Serial.println("CONNECTING...");
      delay(100);
    }  
  }

  while(client.available()){
    char val = client.read();

    if(val== '3'){
      client.print('1');
      digitalWrite(16,LOW);
      delay(50);
      digitalWrite(16,HIGH);
      //digitalWrite(16,HIGH);  
    }  
    if(val == '1'){
      digitalWrite(16,LOW);
      digitalWrite(myRelayCtl,HIGH); //connect the relay
      delay(200);
      digitalWrite(myRelayCtl,LOW); //disconnect
      client.print('1');
      digitalWrite(16,HIGH);  
    }
  }
}
