#include<avr/io.h>
#include<stdbool.h>
int main(void){

bool u,v,z,w,a;
DDRB = 0b00001111; //8&9&10&11 as inputs
PORTB= 0b11110000;
DDRD = 0b00000100; //2as output


while(1)
   {
	   u = (PINB & (1<<PINB0)) == (1<<PINB0);	
	   v = (PINB & (1<<PINB1)) == (1<<PINB1);
	   z = (PINB & (1<<PINB2)) == (1<<PINB2);
	   w = (PINB & (1<<PINB3)) == (1<<PINB3);
	   a=(u&&!z)||(!v&&z)||(!u&&z&&!w);
	   PORTD |= (a<<2);

   }

	return 0;
}
