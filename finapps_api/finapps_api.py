from sense_hat import SenseHat
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    sense = SenseHat()
    X = [255, 0, 0]  # Red
    O = [255, 255, 255]  # White

    question_mark = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, X, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O
    ]

    sense.set_pixels(question_mark)
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')