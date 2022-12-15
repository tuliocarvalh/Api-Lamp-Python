
import requests
from flask import Flask, jsonify
import pyautogui as pg


import serial 

arduino = serial.Serial('COM3', 9600)


app = Flask(__name__) 


@app.route('/')

def homepage() :
    return 'Ok'

@app.route('/ligar_lamp')

def ligar_lamp() :
    arduino.write('l'.encode())
    arduino.flush()
    return jsonify("ok")

@app.route('/desligar_lamp')

def desligar_lamp() :
    arduino.write('d'.encode())
    arduino.flush()
    return jsonify("ok")

app.run()













