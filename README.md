# Rpi-OpenCV-Server

A Raspberry Pi-based vision system that streams video from an Android device and processes it using OpenCV.

## Features
- Live IP camera streaming
- OpenCV video processing
- Web-based video access
- Future GPIO automation (LED, servo)

## Architecture
Android (IP Webcam) → Raspberry Pi → OpenCV → Web Browser

## Endpoints
- `/` → Home page with links
- `/raw` → Original stream
- `/processed` → Processed output (grayscale + edge detection)

## Tech Stack
- Python
- OpenCV
- Flask
- Raspberry Pi

## Setup and Deployment

### Prerequisites
- Raspberry Pi 3 B+ (or compatible)
- Android device with IP Webcam app installed and running
- Python 3.7+ installed on Pi

### Installation
1. Clone or copy this repository to your Raspberry Pi:
   ```bash
   git clone https://github.com/ankits-max/Rpi-OpenCV-Server.git
   cd Rpi-OpenCV-Server
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. On your Android device:
   - Install IP Webcam app
   - Start the server in the app
   - Note the IP address and port (usually 8080)

4. Update `CAMERA_URL` in `app.py` with your Android device's IP Webcam URL (e.g., `http://192.168.1.100:8080/video`)

### Running the Server
```bash
python app.py
```

The server will run on `http://0.0.0.0:5000`. Access from a web browser on the same network.

### Testing
- Visit `http://raspberry-pi-ip:5000` to see the home page
- Click links for raw or processed streams

## Status
✅ Ready to deploy