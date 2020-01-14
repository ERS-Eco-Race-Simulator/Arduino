void on() {
  digitalWrite(13, HIGH); 
}

void off() {
  digitalWrite(13, LOW); 
}

void parse_cmd(int in_byte) {
  if (in_byte == '1') on();
  else off(); 
}

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  while(!Serial) {;}
}

void loop() {
  Serial.write('0');
  if(Serial.available() > 0) {
    int in_byte = Serial.read();
    parse_cmd(in_byte);
  }
}