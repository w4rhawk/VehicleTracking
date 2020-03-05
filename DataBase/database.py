from firebase import firebase
from datetime import datetime
from flask import Flask
from flask import request, jsonify , render_template ,render_template
import markdown
import time
import random
import constants
try:
	firebase = firebase.FirebaseApplication(constants.DATABASE_URI, None)
except Exception as e:
	print(e)
app = Flask(__name__)


@app.route('/')
def index():
        with open("README.md", 'r') as markdown_file:
                content = markdown_file.read()
                return markdown.markdown(content)

@app.route('/AddVehicleData/',methods=["POST"])
def AddVehicleData():
	TollId = request.args['TollId']
	TollLocation = request.args['TollLocation']
	VehicleNumber = request.args['VehicleNumber']
	ArrivalDate = datetime.now().strftime("%d/%m/%Y %H:%M")
	data = {
		"TollId":TollId,
		"TollLocation":TollLocation
	}
	try:
		firebase.post('/'+VehicleNumber+'/'+ArrivalDate+'/',data)
		return jsonify({"Status":"OK"})
	except Exception as e:
		return jsonify({"Status":"NOT OK"})      

@app.route('/getFromDatabase/')
def get():
	VehicleNumber =request.args['VehicleNumber']
	result =firebase.get('/'+VehicleNumber+'/', None)
	return jsonify(result)
	

app.run(debug=True,host="localhost")
