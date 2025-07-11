//  ESP32 air quality monitor
void setup() {
  Serial.begin(115200);
  // initialize sensors here
}

void loop() {
  // read from MQ135 and DHT11, print to serial
  Serial.println("Temp:25.0, Hum:60, Gas:80");
  delay(2000);
}