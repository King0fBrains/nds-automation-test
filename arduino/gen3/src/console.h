#ifndef Console_h
#define Console_h

#define A_PRESS 2
#define B_PRESS 3
#define DOWN_PRESS 9
#define LEFT_PRESS 6
#define RIGHT_PRESS 7
#define SELECT_PRESS 12
#define START_PRESS 13
#define POWER_PIN 14

#define MS_UL(ms) ((ms) * 1000UL) 

#include <Arduino.h>

typedef struct {
  unsigned int delay;
  unsigned int button;
} ButtonDelay;

void openPin(unsigned int pin);
void softResetGameNDS();
void processButtonDelay(ButtonDelay *bd, unsigned int steps);

void waitMicroseconds(unsigned long duration);
void waitMilliseconds(unsigned long duration);

#endif

