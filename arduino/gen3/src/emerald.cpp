#include "console.h"

#define LOAD_INTO_GAME_MS 2263
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))

void deadBatterySeq() {
  ButtonDelay DEAD_BATTERY_SEQ[] = {
    {4191, A_PRESS},
    {838, A_PRESS},
    {355, A_PRESS},
    {3353, A_PRESS},
    {1760, A_PRESS},
    {335, A_PRESS}
  };
  int length = ARRAY_SIZE(DEAD_BATTERY_SEQ);
  processButtonDelay(DEAD_BATTERY_SEQ, length);
}

void liveBatterySeq() {
  ButtonDelay LIVE_BATTERY_SEQ[] = {
    {4191, A_PRESS},
    {838, A_PRESS},
    {355, A_PRESS},
    {335, A_PRESS}
  };
  int length = ARRAY_SIZE(LIVE_BATTERY_SEQ);
  processButtonDelay(LIVE_BATTERY_SEQ, length);
}

void battleRecordSeq() {
  ButtonDelay BATTLE_RECORD[] = {
    {200, DOWN_PRESS},
    {200, DOWN_PRESS},
    {200, DOWN_PRESS},
    {200, DOWN_PRESS},
    {200, A_PRESS}
  };
  int length = ARRAY_SIZE(BATTLE_RECORD);
  processButtonDelay(BATTLE_RECORD, length);
}

void castformSeq() {
  ButtonDelay CASTFORM_SEQ[]  = {
    {0, A_PRESS},
    {645, A_PRESS}
  };
  int length = ARRAY_SIZE(CASTFORM_SEQ);
  processButtonDelay(CASTFORM_SEQ, length);
}

void beldumSeq() {
  ButtonDelay BELDUM_SEQ[] = {
    {0, A_PRESS},
    {838, A_PRESS},
    {754, A_PRESS}
  };
  int length = ARRAY_SIZE(BELDUM_SEQ);
  processButtonDelay(BELDUM_SEQ, length);
}

void wynautSeq() {
  ButtonDelay WYNUAT_SEQ[] = {
    {0, A_PRESS},
    {1375, A_PRESS},
    {1190, A_PRESS},
    {1190, A_PRESS},
    {2084, A_PRESS},
    {1592, A_PRESS},
    {1592, A_PRESS}
  };
  int length = ARRAY_SIZE(WYNUAT_SEQ);
  processButtonDelay(WYNUAT_SEQ, length);
}

void fossilSeqRse() {
  ButtonDelay FOSSIL_RSE_SEQ[] = {
    {0, A_PRESS},
    {671, A_PRESS},
    {1157, A_PRESS}
  };
  int length = ARRAY_SIZE(FOSSIL_RSE_SEQ);
  processButtonDelay(FOSSIL_RSE_SEQ, length);
}

void keckleonSeq() {
  ButtonDelay KECKLEON_SEQ[]  = {
    {0, A_PRESS},
    {1911, A_PRESS},
    {536, A_PRESS},
    {587, A_PRESS},
    {1190, A_PRESS}
  };
  int length = ARRAY_SIZE(KECKLEON_SEQ);
  processButtonDelay(KECKLEON_SEQ, length);
}

void sudowoodoSeq() {
  ButtonDelay SUDOWOODO_SEQ[]  = {
    {0, SELECT_PRESS},
    {4217, A_PRESS},
    {671, A_PRESS}
  };
  int length = ARRAY_SIZE(SUDOWOODO_SEQ);
  processButtonDelay(SUDOWOODO_SEQ, length);
}

void torchicSeq() {
   ButtonDelay TORCHIC_SEQ[] = {
    {0, A_PRESS},
    {0, A_PRESS},
    (1406, A_PRESS)
  };
  int length = ARRAY_SIZE(TORCHIC_SEQ);
  processButtonDelay(TORCHIC_SEQ, length);
}

void mudkipSeq() {
  ButtonDelay MUDKIP_SEQ[] = {
    {0, A_PRESS},
    {0, A_PRESS},
    (1406, RIGHT_PRESS),
    (251, A_PRESS)
  };
  int length = ARRAY_SIZE(MUDKIP_SEQ);
  processButtonDelay(MUDKIP_SEQ, length);
}
void treeckoSeq() {
  ButtonDelay TREECKO_SEQ[] = {
    {0, A_PRESS},
    {0, A_PRESS},
    (1406, LEFT_PRESS),
    (251, A_PRESS)
  };
  int length = ARRAY_SIZE(TREECKO_SEQ);
  processButtonDelay(TREECKO_SEQ, length);
}

void sweetScentSeq() {
  ButtonDelay SWEET_SCENT[] = {
    {0, START_PRESS},
    {200, DOWN_PRESS},
    {200, A_PRESS},
    {2000, DOWN_PRESS},
    {200, A_PRESS},
    {200, DOWN_PRESS},
  };
  int length = ARRAY_SIZE(SWEET_SCENT);
  processButtonDelay(SWEET_SCENT, length);
}

typedef void (*SeqPtr)();

SeqPtr selectSeqRse(int mode) {
  switch (mode) {
    case 1: 
      return fossilSeqRse;
    case 2:
      return castformSeq;
    case 3:
      return beldumSeq;
    case 4:
      return wynautSeq;
    case 5:
      return keckleonSeq;
    case 6:
      return sudowoodoSeq;
    case 7:
      return sweetScentSeq;
    case 8:
      return torchicSeq;
    case 9:
      return mudkipSeq;
    case 10:
      return mudkipSeq;
    case 11:
      return treeckoSeq;
    default:
      return NULL;
  }
  return NULL;
}

void doBattleRecord() {
  openPin(START_PRESS);
  delay(60);
  battleRecordSeq();
  delay(800);
  digitalWrite(LEFT_PRESS, HIGH);
  delay(700);
  digitalWrite(LEFT_PRESS, LOW);

  delay(60);
  digitalWrite(DOWN_PRESS, HIGH);
  delay(300);
  digitalWrite(DOWN_PRESS, LOW);
  delay(60);

  openPin(A_PRESS);
  delay(3823);

  openPin(B_PRESS);
  delay(2200);
  openPin(B_PRESS);
  delay(1200);
  openPin(B_PRESS);
}

void emeraldLoop(unsigned long *seq) {
  softResetGameNDS();
  unsigned long startTimer = micros();

  if (seq[5]){
    Serial.println(F("Beginning live battery sequence..."));
    liveBatterySeq();
  }
  else {
    Serial.println(F("Beginning dead battery sequence..."));
    deadBatterySeq();
  }

  Serial.println(F("Loading into game..."));
  delay(LOAD_INTO_GAME_MS);

  if (seq[1]) {
    Serial.println(F("Commencing battle record..."));
    doBattleRecord();
  }

  if (seq[4] != NULL){
    selectSeqRse(seq[4])();
    Serial.println(F("Mode is not NULL: "));
    Serial.print((uintptr_t)seq[4], HEX);
    Serial.print('\n');
  }
  else {
    Serial.println(F("Mode is NULL"));
    openPin(A_PRESS);
  }

  unsigned long endTimer = micros();
  unsigned long delt = (endTimer - startTimer) / 1000;
  Serial.print(F("Waiting to start encounter: "));
  Serial.print(delt);
  Serial.println(F(" "));

  if (delt < 0) {
    Serial.println(F("Error... Total time was shorter than expected "));
    return;
  }
  unsigned long remainder = seq[3] - delt;
  Serial.println(F(" "));
  if (remainder > seq[3]) {
    Serial.println(F("Error... Total time was shorter than expected"));
    return;
  }

  delay(remainder);
  openPin(A_PRESS);
};
