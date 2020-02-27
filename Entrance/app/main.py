import requests
from appJar import *
import os

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
		self.app.setSize("fullscreen")
		self.app.go()

	def start_process(self):

		data = get_data("TN34")
		self.app.setLabel("t4","Data from database"+str(data))
		data = adddata("TN20","9A","Chennai")
		self.app.setLabel("t5","Data from database"+str(data))




portal = entrance_portal()
