# Vehicle-Tracking
use docker run -d --expose 5003 -p 127.0.0.1:5003:5003/tcp --name=containername imagename for testing
docker logs containername
http://localhost:5003/getFromDatabase/?VehicleNumber=TN34
http://localhost:5003/AddVehicleData/?TollId=2A&TollLocation=Coimbatore&ArrivalDate=2020-02-27%2021%3A32%3A53.338484&EnquiryNumber=9489410269&VehicleNumber=TN10

docker run -d --expose 5002 -p 127.0.0.1:5002:5002/tcp --name=lpdapi licenseplatedetector