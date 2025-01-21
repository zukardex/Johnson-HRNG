int n=0;
void setup() {
  Serial.begin(9600);
    for(int i=0; i<8; i=i+1){
    n=n+ pow(2,i)*digitalRead(i+3);

  }
  Serial.println(n);
}


void loop() {
    Serial.println(n);
    delay(1000);
}
