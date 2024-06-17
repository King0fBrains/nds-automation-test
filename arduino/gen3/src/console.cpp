#include "console.h"

#define POWER_PIN 14

void openPin(unsigned int pin) {
  digitalWrite(pin, HIGH);
  delay(59);
  digitalWrite(pin, LOW);
}

void softResetGameNDS() {
  unsigned int RESET[4] = {2, 3, 12, 13};
  for (int i = 0; i < 4; i++) {
    digitalWrite(RESET[i], HIGH);
  }

  delay(250);

  for (int i = 0; i < 4; i++) {
      digitalWrite(RESET[i], LOW);
    }
}

void rebootConsole() {
  digitalWrite(POWER_PIN, HIGH);
  delay(1000);
  digitalWrite(POWER_PIN, LOW);
  delay(100);

  digitalWrite(POWER_PIN, HIGH);
  delay(1000);
  digitalWrite(POWER_PIN, LOW);
  delay(100);
}

void processButtonDelay(ButtonDelay * bd, unsigned int steps) {
  for (int i = 0; i < steps; i++) {
    
    if (bd[i].delay) {
      Serial.print(F("Delaying for: "));
      Serial.print(bd[i].delay);
      Serial.println(F(" "));
      delay(bd[i].delay);
    }
    Serial.print(F("Pressing: "));
    Serial.print(bd[i].button);
    Serial.println(F(" "));
    openPin(bd[i].button);
  }
}


