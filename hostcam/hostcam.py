from flask import Flask, render_template, Response
import cv2, sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_frame():
    camera = cv2.VideoCapture(int(sys.argv[1]))
    while True:
        _, frame = camera.read()
        jpg_frame = cv2.imencode('.jpg', frame)[1]
        yield (b'--frame\r\nContent-Type: text/plain\r\n\r\n' + jpg_frame.tostring() + b'\r\n')    
    del(camera)

@app.route('/calc')
def calc():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(threaded=True, debug=True, host='0.0.0.0')