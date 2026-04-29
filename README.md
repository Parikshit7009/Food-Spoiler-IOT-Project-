# Food-Spoiler-IOT-Project-
🧊 FridgeGuard – Smart Food Spoilage Detection System
📌 Overview

FridgeGuard is an embedded IoT-based system that monitors food conditions inside a refrigerator using environmental and gas sensors. It detects potential spoilage by analyzing gas concentration changes and provides real-time alerts through a display and buzzer.

🎯 Objectives
Detect food spoilage using gas sensing
Monitor temperature and humidity conditions
Provide real-time visual and audio alerts
Reduce food waste and improve food safety


🧠 Working Principle

The system uses an MQ135 gas sensor to detect changes in air quality caused by gases released during food spoilage. A baseline value is calculated under normal conditions, and any increase from this baseline indicates possible spoilage.

Temperature and humidity are measured using a DHT22 sensor to monitor environmental conditions and help interpret gas variations.

⚙️ Components Used
Raspberry Pi Pico
MQ135 gas sensor
DHT22 temperature and humidity sensor
SSD1306 OLED display
Buzzer
Connecting wires


🔌 Circuit Connections
Component	Pin
MQ135	    GP26 (ADC)
DHT22	    GP14
OLED SDA	GP0
OLED SCL	GP1
Buzzer	    GP15



🧩 Features
Real-time gas monitoring
Temperature & humidity tracking
OLED display output
Buzzer alert system
Dynamic baseline calibration
Simple threshold-based detection


🔄 System Workflow
Sensors → Data Processing → Decision Logic → Output
Read temperature & humidity
Read gas sensor value
Compare with baseline
Classify status:
SAFE
WARNING
SPOILED
Display data on OLED
Trigger buzzer if needed



🚦 Status Logic
Condition	Description
SAFE	No significant gas increase
WARNING	Moderate gas increase
SPOILED	High gas concentration


📊 Example Output
Temp: 25C
Hum: 60%
Gas: 12345
Status: SAFE


⚠️ Limitations
MQ135 is not specific to one gas
Readings affected by temperature and humidity
Requires calibration and warm-up
May produce false positives


🚀 Future Improvements
Integrate temperature & humidity into decision logic
Add WiFi for remote monitoring
Store data for analysis
Use machine learning for better accuracy


🧠 Key Concepts Used
Embedded systems
ADC (Analog to Digital Conversion)
I2C communication
Sensor calibration
Threshold-based decision making


▶️ How to Run
Connect all components correctly
Open Thonny IDE
Upload code to Pico
Save as main.py
Power the system

👉 The system will start automatically