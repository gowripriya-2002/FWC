#include <Arduino.h>
int U,V,Z,W;
int A,B,C,D;
void disp_7447(int D,int C,int B,int A)
{
   digitalWrite(2,A);
}
void setup() {
  pinMode(2, OUTPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
}
void loop() 
{
  U= digitalRead(6);
  V = digitalRead(7);
  Z = digitalRead(8);
  W = digitalRead(9);
 
  A =(U&&!Z)||(!V&&Z)||(!U&&Z&&!W);

  disp_7447(D,C,B,A);

}


