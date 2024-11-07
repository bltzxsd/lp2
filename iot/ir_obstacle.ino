const int irPin = 2;
const int ledPin = 12;

void setup() {
    pinMode(irPin, INPUT);
    pinMode(ledPin, OUTPUT);

    Serial.begin(9600);
}

void loop() {
    int sensorVal = digitalRead(irPin);

    Serial.println(sensorVal);

    if (sensorVal == LOW) {
        Serial.println("Object detected.");
        digitalWrite(ledPin, HIGH);
    } else {
        Serial.println("No object detected.");
        digitalWrite(ledPin, LOW);
    }

    delay(1000);
}
