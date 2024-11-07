#define pin_sel1 13
#define pin_sel2 12
#define pin_sel3 11
#define pin_sel4 10
#define pin_sel5 9

void setup() {
    // Set pin_sel as an output in the setup function
    pinMode(pin_sel1, OUTPUT);
    pinMode(pin_sel2, OUTPUT);
    pinMode(pin_sel3, OUTPUT);
    pinMode(pin_sel4, OUTPUT);
    pinMode(pin_sel5, OUTPUT);
}

void loop() {

    digitalWrite(pin_sel1, LOW);
    digitalWrite(pin_sel2, LOW);
    digitalWrite(pin_sel3, LOW);
    digitalWrite(pin_sel4, LOW);
    digitalWrite(pin_sel5, LOW);

    digitalWrite(pin_sel1, HIGH);
    delay(200);

    digitalWrite(pin_sel1, LOW);
    digitalWrite(pin_sel2, HIGH);
    delay(200);

    digitalWrite(pin_sel2, LOW);
    digitalWrite(pin_sel3, HIGH);
    delay(200);

    digitalWrite(pin_sel3, LOW);
    digitalWrite(pin_sel4, HIGH);
    delay(200);

    digitalWrite(pin_sel4, LOW);
    digitalWrite(pin_sel5, HIGH);
    delay(200);

    digitalWrite(pin_sel5, LOW);
    delay(200);

    digitalWrite(pin_sel1, HIGH);
}