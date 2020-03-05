import requests
from appJar import *
import os
import cv2

def adddata(VehicleNumber,TollId,TollLocation):
	param = {
		"VehicleNumber":VehicleNumber,
		"TollId":TollId,
		"TollLocation":TollLocation
	}
	URL = "http://localhost:5003/AddVehicleData/" 
	
	r = requests.post(url = URL, params=param) 

	data = r.json()

	return data

def get_data(VehicleNumber):

	URL = "http://localhost:5003/getFromDatabase/"
	  
	PARAMS = {'VehicleNumber':VehicleNumber} 
	  
	r = requests.get(url = URL, params = PARAMS) 
	  
	data = r.json()
	  
	return data

def getNumberPlate():
	
	URL = "http://localhost:5002/getPlateNumber/"
	content_type = 'image/jpeg'
	headers = {'content-type': content_type}
	img = cv2.imread('mycar.jpg')
	width=img.shape[1]
	height=img.shape[0]
	hscale_percent = 100
	wscale_percent = 100
	if(height>1500):
		hscale_percent=50
	if(width >1500):
		wscale_percent=50 
	width = int( width* wscale_percent / 100)
	height = int( height* hscale_percent / 100)
	dim = (width, height)
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	_, img_encoded = cv2.imencode('.jpg', resized)  
	r = requests.get(url = URL,data=img_encoded.tostring(), headers=headers) 
	data = r.json()
	return data


class entrance_portal:
	def __init__(self): 
		self.app 			    = gui()
		self.app.setFont(30)
		self.converted_file_data= ""
		self.app.addLabel("s11","",0,0)
		self.app.addLabel("t1", "Welcome to VehicleTracking!!!",0,1)
		self.app.setLabelHeight("t1",5)
		self.app.addLabel("s12","",0,2)
		self.app.addButtons(["Start"], self.start_process,1,1)
		self.app.addLabel("t3","Status:",2,0)
		self.app.addLabel("t4","",2,1)
		self.app.addLabel("t5","",3,1)
		self.app.addLabel("t6","",4,1)
		self.app.setSize("fullscreen")
		self.app.go()
	def start_process(self):
		
		data1 = getNumberPlate()
		data1 = data1[1:-1]
		print(data1)
		self.app.setLabel("t4","Number plate container response"+data1)
		data = adddata(data1,"9A","Chennai")
		self.app.setLabel("t5","Data Upload status"+str(data))
		data = get_data(data1)
		self.app.setLabel("t6","Data from database"+str(data))




portal = entrance_portal()
