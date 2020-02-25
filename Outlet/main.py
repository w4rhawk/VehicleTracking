import requests
from appJar import *
import os


def getNumberPlate():
	
	URL = "http://localhost:5002/getNumberPlate/"
	  
	r = requests.get(url = URL) 

	data = r.json()

	return data

def get_data(userID):

	URL = "http://localhost:5003/getFromDatabase/"
	  
	PARAMS = {'userID':userID} 
	  
	r = requests.get(url = URL, params = PARAMS) 
	  
	data = r.json()
	  
	return data


def update_bal_tran(userID):

	URL = "http://localhost:5003/updateBalTran/"
	  
	PARAMS = {'userID':userID} 
	  
	r = requests.post(url = URL, params = PARAMS) 
	  
	data = r.json()
	  
	return data


class outlet_portal:
	def __init__(self): 
		self.app 			    = gui()
		self.app.setFont(30)
		self.converted_file_data= ""
		self.app.addLabel("s11","",0,0)
		self.app.addFlashLabel("t1", "Thank You and See You Soon!!!",0,1)
		self.app.setLabelHeight("t1",5)
		self.app.addLabel("s12","",0,2)
		self.app.addButtons(["Complete"], self.start_process,1,1)
		self.app.addLabel("t3","Status:",2,0)
		self.app.addLabel("t4","",2,1)
		self.app.setSize("fullscreen")
		self.app.go()

	def start_process(self):

		data1= getNumberPlate()

		print("Number Plate Detection Container response....\n",data1)

		numplate = data1["plate no"]

		user_data = get_data("42A")

		print("User Data from DataBase Container....\n",user_data)

		update_bal_tran("42A")

		p_dat = user_data["name"]+"\nPlate Number :"+user_data["userID"]+"\n"

		self.app.setLabel("t4","You can leave now.. "+p_dat)



portal = outlet_portal()
