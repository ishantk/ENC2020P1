from flask import Flask
from flask import render_template
from flask import Response

import cv2

# pip install imutils
from imutils.video import VideoStream
import imutils

app = Flask(__name__)
videoStream = VideoStream(src=0).start()

@app.route("/")
def index():
    return render_template("videostream.html")

@app.route("/video")
def video():
    return Response(generateFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def generateFrames():
    while True:
        frame = videoStream.read()
        frame = imutils.resize(frame, width=600)
        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

if __name__ == '__main__':
    app.run(debug=True)

# Assignment : Integrate Session67 in Session67A
#              Start Working on Face Recognition Projects: eg: Attendance Management

