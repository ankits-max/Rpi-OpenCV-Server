from flask import Flask, Response
import cv2
import threading

app = Flask(__name__)

# Replace with your IP Webcam URL (e.g., 'http://192.168.1.100:8080/video')
CAMERA_URL = 'http://your-android-ip:8080/video'  # Update this with actual URL

cap = cv2.VideoCapture(CAMERA_URL)

def generate_frames(process=False):
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            if process:
                # Simple OpenCV processing: Convert to grayscale and apply Canny edge detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.Canny(gray, 100, 200)
                # Convert back to BGR for streaming
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/raw')
def raw():
    return Response(generate_frames(process=False), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/processed')
def processed():
    return Response(generate_frames(process=True), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return '''
    <h1>Rpi-OpenCV-Server</h1>
    <p><a href="/raw">Raw Stream</a></p>
    <p><a href="/processed">Processed Stream</a></p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)