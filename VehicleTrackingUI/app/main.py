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
	URL = "http://10.0.75.1:5003/AddVehicleData/" 
	
	r = requests.post(url = URL, params=param) 

	data = r.json()

	return data

def get_data(VehicleNumber):

	URL = "http://10.0.75.1:5003/getFromDatabase/"
	  
	PARAMS = {'VehicleNumber':VehicleNumber} 
	  
	r = requests.get(url = URL, params = PARAMS) 
	  
	data = r.json()
	  
	return data

def getNumberPlate():
	
	URL = "http://10.0.75.1:5002/getPlateNumber/"
	content_type = 'image/jpeg'
	headers = {'content-type': content_type}
	img = cv2.imread('car.jpg')
	# encode image as jpeg
	_, img_encoded = cv2.imencode('.jpg', img)  
	r = requests.get(url = URL,data=img_encoded.tostring(), headers=headers) 

	data = r.json()

	return data


class entrance_portal:
	def __init__(self): 
		self.app 			    = gui()
		self.app.setFont(30)
		self.converted_file_data= ""
		self.app.addLabel("s11","",0,0)
		self.app.addFlashLabel("t1", "Welcome to VehicleTracking!!!",0,1)
		self.app.setLabelHeight("t1",5)
		self.app.addLabel("s12","",0,2)
		self.app.addButtons(["Start"], self.start_process,1,1)
		self.app.addLabel("t3","Status:",2,0)
		self.app.addLabel("t4","",2,1)
		self.app.addLabel("t5","",3,1)
		self.app.addLabel("t6","",4,1)
		self.app.setSize("fullscreen")
		self.app.go()
	def noramlize(self,data):
		normalized = ""
		for i in data:
			if(i != '[' and i != ']' and i != ' ' and i != '\"' and i != '-'):
				if(i==','):
					normalized=""
					continue
				if(i=='.'):
					continue
				normalized+=i
		return normalized
	def start_process(self):
		
		data1 = getNumberPlate()
		data1 = self.noramlize(data1)
		print(data1)
		self.app.setLabel("t4","Number plate container response"+data1)
		data = adddata(data1,"9A","Chennai")
		self.app.setLabel("t5","Data Upload status"+str(data))
		data = get_data(data1)
		self.app.setLabel("t6","Data from database"+str(data))




portal = entrance_portal()
