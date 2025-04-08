/* 
 * Created by Linh Huynh
 * Created on April 2025
 * 
*/

# include <Servo.h>
Servo servoNumber1;

// constants
int popin = 0;
int IN_MIN = 0;
int OUT_MAX = 180;
int IN_MAX = 1023;
int OUT_MIN = 0;

//variable
float duration;
float distance;
float val;

//setup
void setup() {
    // setup servo pins, controls
    servoNumber1.attach(9);
    servoNumber1.write(0);
  
}

void loop() {
  
    val = analogRead(popin);
    val = (val/6);
    servoNumber1.write(val);
    delay(15);
  
}
