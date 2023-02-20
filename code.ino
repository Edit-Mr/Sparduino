#include <Adafruit_SSD1306.h>
#include <Wire.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  Serial.begin(9600);
  Wire.begin();
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextColor(WHITE);
  display.setTextSize(2);
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readString();
    display.clearDisplay();
    display.setCursor(0, 0);
    int lastIndex = 0;
    int newIndex = message.indexOf("/");
    while (newIndex != -1) {
      display.println(message.substring(lastIndex, newIndex));
      lastIndex = newIndex + 1;
      newIndex = message.indexOf("/", lastIndex);
    }
    display.println(message.substring(lastIndex));
    display.display();
  }
}

