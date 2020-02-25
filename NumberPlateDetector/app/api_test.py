import io
import os
from google.cloud import vision
from datetime import datetime
import cv2
import time
import random

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_key.json'

from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('1.jpg')

img = cv2.imread(file_name)
# Get image size
height, width = img.shape[:2]
# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)


# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations


#print(response)
response = client.annotate_image({'image': image })

#response = client.annotate_image(request)

print(response)

cor=response.localized_object_annotations[0].bounding_poly

vertices = [(vertex.x*height, vertex.y*width) for vertex in cor.normalized_vertices]

print(vertices)

print(vertices[0][0]-10, vertices[0][1]-10,vertices[2][0]+10, vertices[2][1]+10)       
cv2.rectangle(img, (int(vertices[0][0])-10, int(vertices[0][1])-10), (int(vertices[2][0])+15, int(vertices[2][1])+10), (0, 255, 0), 2)
cv2.imwrite("output.jpg", img)

img = cv2.imread(file_name)

crop_img = img[int(vertices[0][1]):int(vertices[2][1]), int(vertices[0][0]):int(vertices[2][0])+15]
cv2.imshow("cropped", crop_img)
cv2.imwrite("temp.jpg", crop_img)

cv2.waitKey(0)

with io.open("temp.jpg", 'rb') as image_file:
        content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations

print(texts)