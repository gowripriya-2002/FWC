//----------------------Skeleton Code--------------------//
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

//    Can be client or even host   //
#ifndef STASSID
#define STASSID "A.G.P.R" // Add your network credentials
#define STAPSK  "gangagowri123"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;


void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}

//-------------------------------------------------------//
int U,V,Z,W;
int A,B,C,D;
void disp_7447(int D,int C,int B,int A);
{
  digitalwrite(2,A);
}
void setup(){
  OTAsetup();
  pinMode(2, OUTPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);

  //-------------------//
  // Custom setup code //
  //-------------------//
}

void loop() {
  OTAloop();
  U = digitalRead(6);
  V = digitalRead(7);
  Z= digitalRead(8);
  W= digitalRead(9);
  A = (U&&!Z) || (!V&&Z)||(!U&&Z&&!W);
  disp_7447(D,C,B,A);
  delay(10);  // If no custom loop code ensure to have a delay in loop
  //-------------------//
  // Custom loop code  //
  //-------------------//
}
