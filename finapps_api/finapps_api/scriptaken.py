from sense_hat import SenseHat
import RPi.GPIO as GPIO
import sqlite3
import time
import json

def hello_world():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.IN)

    B = [0,0,0] #negre
    X = [100,100,100] #blanc gris
    V = [255,150,0] #tronja
    K = [0, 150, 150]

    cares = [ 
    [B,B,B,B,B,B,B,B,
    X,X,X,B,B,X,X,X,
    X,B,X,B,B,X,B,X,
    B,B,B,B,B,B,B,B,
    B,V,V,V,V,V,V,B,
    B,B,V,V,V,V,B,B,
    B,B,B,V,V,B,B,B,
    B,B,B,B,B,B,B,B]
    ,
    [B,B,B,B,B,B,B,B,
    X,X,B,B,B,B,X,X,
    B,B,X,B,B,X,B,B,
    B,B,B,B,B,B,B,B,
    B,V,V,V,V,V,V,B,
    B,B,V,V,V,V,B,B,
    B,B,B,V,V,B,B,B,
    B,B,B,B,B,B,B,B]
    ,
    [B,B,B,B,B,B,B,B,
    B,B,B,B,B,B,B,B,
    X,X,X,B,B,X,X,X,
    B,B,B,B,B,B,B,B,
    B,V,V,V,V,V,V,B,
    B,B,V,V,V,V,B,B,
    B,B,B,V,V,B,B,B,
    B,B,B,B,B,B,B,B]
    ,
    [B,B,B,B,B,B,B,B,
    B,B,X,B,B,X,B,B,
    X,X,B,B,B,B,X,X,
    B,B,B,B,B,B,B,B,
    B,V,V,V,V,V,V,B,
    B,B,V,V,V,V,B,B,
    B,B,B,V,V,B,B,B,
    B,B,B,B,B,B,B,B]
    ,
    [B,B,B,B,B,B,B,B,
    X,B,X,B,B,X,B,X,
    X,X,X,B,B,X,X,X,
    B,B,B,B,B,B,B,B,
    B,V,V,V,V,V,V,B,
    B,B,V,V,V,V,B,B,
    B,B,B,V,V,B,B,B,
    B,B,B,B,B,B,B,B]
    ,
    [B,B,B,B,B,B,B,B,
    X,X,X,B,B,X,X,X,
    X,K,X,B,B,X,K,X,
    B,B,B,B,B,B,B,B,
    B,V,V,V,V,V,V,B,
    B,B,V,V,V,V,B,B,
    B,B,B,V,V,B,B,B,
    B,B,B,B,B,B,B,B]
    ]

    caraActual = 2
    
    sense = SenseHat()
    sense.set_rotation(270)

    start = time.time()
    elapsedTime = 0

    elapsedTime_sett = 0

    # Initialize config
    with open('../config.json', 'r') as content_file:
        content = content_file.read()

    config = json.loads(content)

    sense.set_pixels(cares[caraActual])

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    deltat = 604800
    
    while True:
        if elapsedTime > 3 and elapsedTime < 5:
            sense.set_pixels(cares[5])
        else:
            sense.set_pixels(cares[caraActual])

        if elapsedTime_sett > 5:
            with open('../config.json', 'r') as content_file:
                content = content_file.read()
            config = json.loads(content)
            elapsedTime_sett = 0
        
        if elapsedTime > 1 and GPIO.input(7) == 1:
            print(elapsedTime)
            elapsedTime = 0
            if config['action'] == "negative":
                caraActual += 1
            else:
                caraActual -= 1
            cursor.execute("INSERT INTO entries (date, amount, delayed_until, reason) VALUES (?,?,?,?)", [int(time.time()), config['quantity'], int(time.time() + deltat), config['reason']])
            conn.commit()
        
        end = time.time()
        dif = end - start
        elapsedTime += dif
        elapsedTime_sett += dif
        start = time.time()
        
        if elapsedTime > 20:
            if config['action'] == "negative":
                caraActual -= 1
            else:
                caraActual += 1
            elapsedTime = 0

        if caraActual > 4:
            caraActual = 4
        if caraActual < 0:
            caraActual = 0

hello_world()            