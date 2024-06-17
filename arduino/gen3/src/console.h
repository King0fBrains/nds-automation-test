#ifndef Console_h
#define Console_h

#define A_PRESS 2
#define B_PRESS 3
#define DOWN_PRESS 9
#define LEFT_PRESS 6
#define RIGHT_PRESS 7
#define SELECT_PRESS 12
#define START_PRESS 13

#include <Arduino.h>

typedef struct {
  unsigned int delay;
  unsigned int button;
} ButtonDelay;

void openPin(unsigned int pin);
void softResetGameNDS();
void processButtonDelay(ButtonDelay *bd, unsigned int steps);

#endif

