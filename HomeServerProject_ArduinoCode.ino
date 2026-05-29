#include <Servo.h>

const int LED_PIN = 7;
const int SERVO_PIN = 9;

Servo myservo;

void setup() {

  // LED setup
  pinMode(LED_PIN, OUTPUT);

  // Serial communication
  Serial.begin(9600);

  // Servo setup
  myservo.attach(SERVO_PIN);

  // Start position
  myservo.write(0);
}

void loop() {

  // Check if serial data exists
  if (Serial.available()) {

    // Read incoming command
    String command = Serial.readStringUntil('\n');

    // Remove extra spaces/newlines
    command.trim();


    // ----------------------------
    // LED CONTROLS
    // ----------------------------

    if (command == "LED_ON") {
      digitalWrite(LED_PIN, HIGH);
    }

    else if (command == "LED_OFF") {
      digitalWrite(LED_PIN, LOW);
    }


    // ----------------------------
    // PRESET SERVO POSITIONS
    // ----------------------------

    else if (command == "SERVO_0") {
      myservo.write(0);
    }

    else if (command == "SERVO_90") {
      myservo.write(90);
    }


    else if (command == "SERVO_180") {
      myservo.write(180);
    }


    // ----------------------------
    // CUSTOM SERVO ANGLE
    // Example:
    // SERVO:73
    // ----------------------------

    else if (command.startsWith("SERVO:")) {

      // Extract angle after "SERVO:"
      int angle = command.substring(6).toInt();

      // Safety limits
      if (angle < 0) {
        angle = 0;
      }

      if (angle > 180) {
        angle = 180;
      }

      // Move servo
      myservo.write(angle);
    }
  }
}