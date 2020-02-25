from firebase import firebase
from datetime import datetime
import cv2
from flask import Flask
from flask import request, jsonify , render_template ,render_template
import markdown
import time
import random


firebase = firebase.FirebaseApplication('database link', None)
app = Flask(__name__)


@app.route('/')
def index():
        with open("README.md", 'r') as markdown_file:
                content = markdown_file.read()
                return markdown.markdown(content)

@app.route('/updateSession/',methods=["POST"])
def updateSession():
	userID 	  =request.args['userID']
	slot      =random.randint(10,130)
	start_time=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	try:
		firebase.put('/user/'+userID,"session",{"start_time":start_time,"slot_alloted":slot})
		return jsonify({"Status":"OK"})
	except Exception as e:
		return jsonify({"Status":"NOT OK"})      

@app.route('/updateBalTran/',methods=["POST"])
def updateBalTran():
	userID 	    =request.args['userID']
	result      =firebase.get('/user/'+userID, None)
	transaction =result["trans"]
	balance     =result["balance"]-50
	end_time    =datetime.now().strftime("%d/%m/%Y %H:%M:%S")
	new_trans   ={"start_time":result["session"]["start_time"],"end_time":end_time,"fee_paid":50.0}
	transaction.append(new_trans)

	try:
		firebase.put('/user/'+userID,"trans",transaction)
		firebase.put('/user/'+userID,"balance",balance)
		return jsonify({"Status":"OK"})
	except Exception as e:
		return jsonify({"Status":"NOT OK"})      


@app.route('/getFromDatabase/')
def get():
	userID =request.args['userID']
	result =firebase.get('/user/'+userID, None)
	return jsonify(result)
	

app.run(debug=True,host="localhost")
