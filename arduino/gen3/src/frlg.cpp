#include "console.h"

#define LOAD_INTO_GAME_MS 2680
#define WAIT_FOR_SAV_MENU 3950
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))

void fossilSeqFrlg() {
  ButtonDelay FOSSIL_SEQ[] = {
    {0, A_PRESS},
    {1509, A_PRESS}
  };
  int length = ARRAY_SIZE(FOSSIL_SEQ);
  processButtonDelay(FOSSIL_SEQ, length);
}

void starterSeq() {
  ButtonDelay STARTER_SEQ[] = {
    {0, A_PRESS},
    {2095, A_PRESS},
    {1173, A_PRESS}
  };
  int length = ARRAY_SIZE(STARTER_SEQ);
  processButtonDelay(STARTER_SEQ, length);
}

void snorlaxSeq() {
  ButtonDelay SNORLAX_SEQ[] = {
    {0, A_PRESS},
    {1006, A_PRESS},
    {8581, A_PRESS}
  };
  int length = ARRAY_SIZE(SNORLAX_SEQ);
  processButtonDelay(SNORLAX_SEQ, length);
}

void hypnoSeq() {
  ButtonDelay HYPNO_SEQ[] = {
    {0, A_PRESS},
    {1341, A_PRESS},
    {1090, A_PRESS},
    {1006, A_PRESS},
    {2180, A_PRESS},
    {2012, A_PRESS}
  };
  int length = ARRAY_SIZE(HYPNO_SEQ);
  processButtonDelay(HYPNO_SEQ, length);
}

void laprasSeq() {
  ButtonDelay LAPRAS_SEQ[] = {
    {0, A_PRESS},
    {1274, A_PRESS},
    {503, A_PRESS}
  };
  int length = ARRAY_SIZE(LAPRAS_SEQ);
  processButtonDelay(LAPRAS_SEQ, length);
}

void magikarpSeq() {
  ButtonDelay MAGIKARP_SEQ[] = {
    {0, A_PRESS},
    {1005, A_PRESS},
    {1676, A_PRESS}
  };
  int length = ARRAY_SIZE(MAGIKARP_SEQ);
  processButtonDelay(MAGIKARP_SEQ, length);
}

void togepiSeq() {
  ButtonDelay TOGEPI_SEQ[] = {
    {0, A_PRESS},
    {1173, A_PRESS},
    {1006, A_PRESS},
    {1173, A_PRESS},
    {922, A_PRESS},
    {922, A_PRESS}
  };
  int length = ARRAY_SIZE(TOGEPI_SEQ);
  processButtonDelay(TOGEPI_SEQ, length);
}

void sweetScentFRLG() {
  ButtonDelay SWEET_SCENT_FRLG[] = {
    {0, START_PRESS},
    {200, DOWN_PRESS},
    {200, A_PRESS},
    {2000, DOWN_PRESS},
    {200, A_PRESS},
    {200, DOWN_PRESS}
  };
  int length = ARRAY_SIZE(SWEET_SCENT_FRLG);
  processButtonDelay(SWEET_SCENT_FRLG, length);
}

void abraSeq() {
  ButtonDelay ABRA_GC_SEQ[] = {
    {0, A_PRESS},
    {2012, A_PRESS},
    {2012, A_PRESS}
  };
  int length = ARRAY_SIZE(ABRA_GC_SEQ);
  processButtonDelay(ABRA_GC_SEQ, length);
};

void clefairySeq() {
  ButtonDelay CLEFAIRY_GC_SEQ[] = {
    {0, A_PRESS},
    {2012, A_PRESS},
    {2012, DOWN_PRESS},
    {60, A_PRESS}
  };
  int length = ARRAY_SIZE(CLEFAIRY_GC_SEQ);
  processButtonDelay(CLEFAIRY_GC_SEQ, length);
}

void dratiniSeq() {
  ButtonDelay DRATINI_GC_SEQ[] = {
    {0, A_PRESS},
    {2012, A_PRESS},
    {2012, DOWN_PRESS},
    {60, DOWN_PRESS},
    {60, A_PRESS}
  };
  int length = ARRAY_SIZE(DRATINI_GC_SEQ);
  processButtonDelay(DRATINI_GC_SEQ, length);
}

void scypinSeq() {
  ButtonDelay SCYPIN_GC_SEQ[] = {
    {0, A_PRESS},
    {2012, A_PRESS},
    {2012, DOWN_PRESS},
    {60, DOWN_PRESS},
    {60, DOWN_PRESS},
    {60, A_PRESS}
  };
  int length = ARRAY_SIZE(SCYPIN_GC_SEQ);
  processButtonDelay(SCYPIN_GC_SEQ, length);
}

void porygonSeq() {
  ButtonDelay PORYGON_GC_SEQ[] = {
    {0, A_PRESS},
    {2012, A_PRESS},
    {2012, DOWN_PRESS},
    {60, DOWN_PRESS},
    {60, DOWN_PRESS},
    {60, DOWN_PRESS},
    {60, A_PRESS}
  };
  int length = ARRAY_SIZE(PORYGON_GC_SEQ);
  processButtonDelay(PORYGON_GC_SEQ, length);
}

typedef void (*SeqPtr)();

SeqPtr selectSeqFrlg(int mode) {
  switch (mode) {
    case 1: 
      return fossilSeqFrlg;
    case 2:
      return starterSeq;
    case 4:
      return magikarpSeq;
    case 5:
      return laprasSeq;
    case 6:
      return togepiSeq;
    case 7:
      return sweetScentFRLG;
    case 8:
      return abraSeq;
    case 9:
      return clefairySeq;
    case 10:
      return dratiniSeq;
    case 11:
      return scypinSeq;
    case 12:
      return porygonSeq;
    case 13:
      return snorlaxSeq;
    default:
      return NULL;
  }
  return NULL;
}

void teachyTV(unsigned long timer) {
  unsigned long startTimer = millis();
  openPin(SELECT_PRESS);
  delay(1200);
  unsigned long endTimer = millis();
  unsigned long waitTime = timer - (endTimer - startTimer);

  if (waitTime < 0) 
    return
    
  Serial.println(waitTime);
  delay(waitTime);
  openPin(B_PRESS);
  delay(1000);
}

void frlgLoop(unsigned long *seq) {
  if (seq[1]){
    digitalWrite(SELECT_PRESS, HIGH);
    Serial.println(F("Holding select..."));
  }

  unsigned long startTimer = micros();
  Serial.println(F("Waiting thru intro timer..."));
    openPin(A_PRESS);
    delay(seq[2]);

  Serial.println(F("Intro complete..."));
    digitalWrite(seq[5], HIGH);
    delay(WAIT_FOR_SAV_MENU);

  if (seq[1]){
    Serial.println(F("Select released...")); 
      digitalWrite(SELECT_PRESS, LOW);
  }

  digitalWrite(seq[5], LOW);
  delay(60);
  openPin(A_PRESS);
  delay(LOAD_INTO_GAME_MS);
  openPin(B_PRESS);
  delay(LOAD_INTO_GAME_MS);

  Serial.println(F("Loaded into game..."));
  if (seq[6] > 0)
    teachyTV(seq[6]);
  
  if (seq[4] != 0){
    Serial.print(F("Mode is not NULL: 0x"));
    Serial.print((uintptr_t)seq[4], HEX);
    Serial.println(F(" "));
    selectSeqFrlg(seq[4])();
  }
  else {
    Serial.println(F("Mode is NULL"));
    openPin(A_PRESS);
  }

  unsigned long endTimer = micros();
  unsigned long delt = (endTimer - startTimer) / 1000;
  Serial.print(F("Waiting to start encounter: "));
  Serial.print(delt);
  Serial.print('\n');

  if (delt < 0) {
    Serial.println(F("Error... Total time was shorter than expected"));
    return;
  }

  delay(seq[3] - delt);
  openPin(A_PRESS);
}
