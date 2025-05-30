# ESP32 Camera + YOLOv8 Object Detection

This project streams video from an ESP32-CAM over Wi-Fi and uses a YOLOv8 model on a computer (Python + OpenCV) for real-time object detection.

---

## 📷 ESP32-CAM

The ESP32 runs a lightweight HTTP server that streams MJPEG video frames over Wi-Fi.

### 🔧 Hardware Used
- ESP32-CAM (AI Thinker)
- Wi-Fi network (2.4 GHz)

### 🔌 Pin Configuration
Pre-configured for AI Thinker module:

### ⚙️ Upload Instructions
1. Open `esp32/camera_stream.ino` in Arduino IDE or PlatformIO.
2. Replace the Wi-Fi credentials:
```cpp
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
1.Select the correct board (ESP32 Wrover Module or AI Thinker).

2.Upload the code.

3.Open Serial Monitor to get the IP address.
🧠 YOLOv8 Detection (Python)
Once the stream is live, use the detect.py script to analyze the video feed with Ultralytics YOLOv8.

🧰 Requirements
Install dependencies:
pip install -r requirements.txt
requirements.txt
ultralytics
opencv-python
matplotlib
🎯 Run the detection
Update your ESP32 IP in the script (e.g., http://192.168.0.xxx/):
python python/detect.py
