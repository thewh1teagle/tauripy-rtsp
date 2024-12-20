"""
http://localhost:8090/
"""
import time
import cv2
from flask import Flask, Response

# RTSP stream URL
rtsp_url = "rtsp://127.0.0.1:8554/stream"

app = Flask(__name__)

# setup camera and resolution
cam = cv2.VideoCapture(rtsp_url)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
def gather_img():
    while True:
        time.sleep(0.1)
        _, img = cam.read()
        _, frame = cv2.imencode('.jpg', img)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

@app.route("/mjpeg")
def mjpeg():
    return Response(gather_img(), mimetype='multipart/x-mixed-replace; boundary=frame')

def run_mjpg_server():
    app.run(host='0.0.0.0', threaded=True)