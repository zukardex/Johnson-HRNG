const int analogPin = A0;  
void setup() {
    Serial.begin(9600); 
    randomSeed(analogRead(A1));  // Seed random generator with floating pin noise
}

void loop() {
    int sensorValue = analogRead(analogPin); 
    float voltage = (sensorValue / 1023.0) * 5.0; 
    

    float noise = (random(0, 50) / 1000.0); 
    float noisyVoltage = (voltage * 5) + noise;
    
    if (random(0, 10) > 3) {
        Serial.println(noisyVoltage);
    }
}
