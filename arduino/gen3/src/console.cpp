#include "console.h"

void waitMicroseconds(unsigned long duration) {
  unsigned long start = micros();
  while ((micros() - start) < duration) {
  }
}

void waitMilliseconds(unsigned long duration) {
  unsigned long start = millis();
  while ((millis() - start) < duration) {
  }
}

void openPin(unsigned int pin) {
  digitalWrite(pin, HIGH);
  waitMicroseconds(MS_UL(59));
  digitalWrite(pin, LOW);
}

void softResetGameNDS() {
  unsigned int RESET[4] = {A_PRESS, B_PRESS, SELECT_PRESS, START_PRESS};
  for (int i = 0; i < 4; i++) {
    digitalWrite(RESET[i], HIGH);
  }

  waitMicroseconds(MS_UL(250));

  for (int i = 0; i < 4; i++) {
      digitalWrite(RESET[i], LOW);
    }
}

void rebootConsole() {
  digitalWrite(POWER_PIN, HIGH);
  waitMicroseconds(MS_UL(1000));

  digitalWrite(POWER_PIN, LOW);
  waitMicroseconds(MS_UL(1000));
  
  digitalWrite(POWER_PIN, HIGH);
  waitMicroseconds(MS_UL(1000));

  digitalWrite(POWER_PIN, LOW);
  waitMicroseconds(MS_UL(1000));
}

void processButtonDelay(ButtonDelay * bd, unsigned int steps) {
  for (int i = 0; i < steps; i++) {
    
    if (bd[i].delay) {
      Serial.print(F("Delaying for: "));
      Serial.print(bd[i].delay);
      Serial.println(F(" "));
      waitMicroseconds(MS_UL(bd[i].delay));
    }
    Serial.print(F("Pressing: "));
    Serial.print(bd[i].button);
    Serial.println(F(" "));
    openPin(bd[i].button);
  }
}


