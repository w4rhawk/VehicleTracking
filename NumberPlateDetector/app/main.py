import io
import os
from google.cloud import vision
from datetime import datetime
import cv2
from flask import Flask
from flask import request, jsonify , render_template ,render_template
import markdown
import time
import random

PEOPLE_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_key.json'

img_path = '1.jpg'

def recognize_license_plate():
    
    global img_path

    start_time = datetime.now()

    # Read image with opencv
    img = cv2.imread(img_path)
    cv2.imshow("dffs",img)

    # Get image size
    height, width = img.shape[:2]

    # Scale image
    img = cv2.resize(img, (800, int((height * 800) / width)))

    # Save the image to temp file
    cv2.imwrite("output.jpg", img)

    # Create new img path for google vision
    img_path =  "output.jpg"

    # Create google vision client
    client = vision.ImageAnnotatorClient()

    # Read image file
    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    # Recognize text
    response = client.text_detection(image=image)
    texts = response.text_annotations
    print(texts)
    for text in texts:
        if len(text.description) == 10:
            license_plate = text.description
            vertices = [(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices]

            # Put text license plate number to image
            cv2.putText(img, license_plate, (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

            # Draw rectangle around license plate
            cv2.rectangle(img, (vertices[0][0]-10, vertices[0][1]-10), (vertices[2][0]+10, vertices[2][1]+10), (0, 255, 0), 3)
            cv2.imwrite(os.path.join(PEOPLE_FOLDER, "output.jpg"), img)
            return license_plate,vertices


@app.route('/')
def index():
        with open("README.md", 'r') as markdown_file:
                content = markdown_file.read()
                return markdown.markdown(content)

@app.route('/getNumberPlate/', methods=['GET'])
def getNumberPlate():

    Number,Coordinates=recognize_license_plate()
    #Number,Coordinates = "37A-401.57",[[234,433],[324,543],[434,565],[434,122]]
    json_data= {
                    "identifier": "NumberPlate",
                    "plate no":Number,
                    "Coordinates":Coordinates,
                    "message":"success",
                    "time"   :time.ctime(),
                }

    return jsonify(json_data), 201

@app.route('/getDetectedImage/')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img.jpg')
    return render_template("index.html", user_image = full_filename)

app.run(debug=True,host="0.0.0.0",port=5002)