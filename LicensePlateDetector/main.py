import cv2
from flask import Flask
from flask import request, jsonify , render_template ,render_template
import json
import numpy as np 
import DetectPlates

app = Flask(__name__)
@app.route('/')
def index():
    return "License Plate Detector API"   

@app.route('/getPlateNumber/')
def getPlateNumber():
    r=request
    nparr = np.fromstring(r.data,np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)    
    plateno = DetectPlates.getPlateNumber(image)
    return jsonify(json. dumps(plateno))

app.run(debug=True,host="0.0.0.0",port=5002)