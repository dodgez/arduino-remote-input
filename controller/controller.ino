#define LT_INPUT_PIN 2
#define MD_INPUT_PIN 3
#define RT_INPUT_PIN 4

void setup() {
  pinMode(LT_INPUT_PIN, INPUT_PULLUP);
  pinMode(MD_INPUT_PIN, INPUT_PULLUP);
  pinMode(RT_INPUT_PIN, INPUT_PULLUP);

  Serial.begin(9600);
}

bool keyWasPressed[3] = {false};

void handleButton(int pin, int btnPressedIndex) {
  bool buttonPressed = !digitalRead(pin);

  if (buttonPressed && !keyWasPressed[btnPressedIndex]) {
    Serial.print(btnPressedIndex);
    keyWasPressed[btnPressedIndex] = true;
  }

  if (!buttonPressed && keyWasPressed[btnPressedIndex]) {
    Serial.print(btnPressedIndex | 4);
    keyWasPressed[btnPressedIndex] = false;
  }
}

void loop() {
  handleButton(LT_INPUT_PIN, 0);
  handleButton(MD_INPUT_PIN, 1);
  handleButton(RT_INPUT_PIN, 2);

  delay(50);
}
