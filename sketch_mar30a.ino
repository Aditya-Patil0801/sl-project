#include <DHT.h>

// DHT setup
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

// MQ Sensors
int mq135 = A0;
int mq7 = A1;

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {

  int air = analogRead(mq135);
  int co = analogRead(mq7);

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  // Handle sensor error
  if (isnan(temp) || isnan(hum)) {
    // Send dummy values to keep CSV format
    Serial.println("0,0,0,0");
  } else {
    // ✅ ONLY CSV FORMAT (VERY IMPORTANT)
    Serial.print(air);
    Serial.print(",");
    Serial.print(co);
    Serial.print(",");
    Serial.print(temp);
    Serial.print(",");
    Serial.println(hum);
  }

  delay(15000);  // 15 seconds delay
}