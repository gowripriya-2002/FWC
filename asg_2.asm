;logical AND, OR and XOR operations
;output displayed using 7447 IC

.include "/home/student/m328Pdef.inc"

ldi r16, 0b00111100 ;identifying output pins 2,3,4,5
out DDRD,r16		;declaring pins as output



ldi r16,0b00000001	;initializing U
ldi r17,0b00000000	;initializing V
ldi r18,0b00000001	;initializing Z
ldi r19,0b00000000  ;initializing W


ldi r23,0b00000001
eor r23,r18       ;z!
AND r16,r23        ;u&&!z
ldi r24,0b00000001 
eor r24,r17        ;!v
AND r18,r24        ;!v&&z
ldi r25,0b00000001
eor r25,r16        ; !u 
ldi r26,0b00000001
eor r26,r19        ;!w
AND r25,r18         ;!u&z
AND r25,r26        ;!u&z&!w
OR r16,r18,r25     ;(u&&!z)+(!v&&z)+(!u&z&!w)


;following code is for displaying output
;shifting LSB in r16 to 2nd position
ldi r20, 0b00000010	;counter = 2

rcall loopw		;calling the loopw routine

out PORTD,r16		;writing output to pins 2,3,4,5


Start:
rjmp Start

;loop for bit shifting
loopw:	lsl r16 	;left shift
	dec r20			;counter --
	brne loopw	;if counter != 0
	ret
