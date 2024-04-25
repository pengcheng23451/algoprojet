#include <MKRWAN.h>

LoRaModem modem;

// Initialisation du module LoRa
String appEui = "a8610a34353b7210";
String appKey = "07070707070707070707070707070707";

void setup() {
  Serial.begin(9600);
  while (!Serial);
  if(!modem.begin(EU868)){
    Serial.println("inavailable to start module");
    while (1){} // if lora fail, the execution will stop 
  };
  Serial.print("Your module version is: ");
  Serial.println(modem.version());
  Serial.print("Your device EUI is: ");
  Serial.println(modem.deviceEUI());

  int connected = modem.joinOTAA(appEui,appKey);
  if(!connected){
    Serial.println("Something was wrong.");
    while (1){}
  } 
  modem.minPollInterval(60);
}


void loop() {
  // Simulation du déplacement aléatoire des animaux
  String myList[] = {"chien", "chat", "chevaux"};
  int animalPositionX = random(-200, 200);
  int animalPositionY = random(-200, 200);
  int randomIndex = random(0, sizeof(myList)/sizeof(myList[0]));

  // Construire un message
  String message = "Animal position: X=" + String(animalPositionX) + "; Y=" + String(animalPositionY);

  // Envoyer un message
  modem.beginPacket();
  modem.print(message);
  modem.endPacket();

  Serial.println("Message: " + message);

  // 等待一段时间再发送下一条消息
  delay(15000); // 每 15 秒发送一次消息
}