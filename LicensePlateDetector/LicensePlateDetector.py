import cv2
import imagetotext
from flask import Flask
from flask import request, jsonify , render_template ,render_template
import json
import numpy as np 

app = Flask(__name__)
watch_cascade = cv2.CascadeClassifier('cascade.xml')

def detectPlateRough(image_gray,resize_h = 720,en_scale =1.08 ,top_bottom_padding_rate = 0.05):
        if top_bottom_padding_rate>0.2:
            print("error:top_bottom_padding_rate > 0.2:",top_bottom_padding_rate)
            exit(1)
        height = image_gray.shape[0]
        padding = int(height*top_bottom_padding_rate)
        scale = image_gray.shape[1]/float(image_gray.shape[0])
        image = cv2.resize(image_gray, (int(scale*resize_h), resize_h))
        image_color_cropped = image[padding:resize_h-padding,0:image_gray.shape[1]]
        image_gray = cv2.cvtColor(image_color_cropped,cv2.COLOR_RGB2GRAY)
        watches = watch_cascade.detectMultiScale(image_gray, en_scale, 2, minSize=(36, 9),maxSize=(36*40, 9*40))
        cropped_images = []
        i=1
        plateno=[]
        for (x, y, w, h) in watches:

            #cv2.rectangle(image_color_cropped, (x, y), (x + w, y + h), (0, 0, 255), 1)

            x -= w * 0.14
            w += w * 0.28
            y -= h * 0.15
            h += h * 0.3

            #cv2.rectangle(image_color_cropped, (int(x), int(y)), (int(x + w), int(y + h)), (0, 0, 255), 1)
            name="plate"+str(i)+".jpg"
            text = cropImageandGettext(image_color_cropped, (int(x), int(y), int(w), int(h)),name)
            #cropped_images.append([cropped,[x, y+padding, w, h]])
            plateno.append(text)
            i=i+1
            #cv2.imshow("imageShow", cropped)
            #cv2.waitKey(0)
        return plateno

def cropImageandGettext(image,rect,name):
        #cv2.imshow("imageShow", image)
        #cv2.waitKey(0)
        x, y, w, h = computeSafeRegion(image.shape,rect)
        #cv2.imshow("imageShow", image[y:y+h,x:x+w])
        cv2.imwrite(name,image[y:y+h,x:x+w])
        plateno=imagetotext.get_string(name)
        #cv2.waitKey(0)
        #return image[y:y+h,x:x+w]
        return plateno


def computeSafeRegion(shape,bounding_rect):
        top = bounding_rect[1] # y
        bottom  = bounding_rect[1] + bounding_rect[3] # y +  h
        left = bounding_rect[0] # x
        right =   bounding_rect[0] + bounding_rect[2] # x +  w
        min_top = 0
        max_bottom = shape[0]
        min_left = 0
        max_right = shape[1]

        #print(left,top,right,bottom)
        #print(max_bottom,max_right)

        if top < min_top:
            top = min_top
        if left < min_left:
            left = min_left
        if bottom > max_bottom:
            bottom = max_bottom
        if right > max_right:
            right = max_right
        return [left,top,right-left,bottom-top]

@app.route('/')
def index():
    return "License Plate Detector API"   

@app.route('/getPlateNumber/')
def getPlateNumber():
    r=request
    nparr = np.fromstring(r.data,np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)    
    plateno = detectPlateRough(image,image.shape[0],top_bottom_padding_rate=0.1)
    for i in plateno:
        print(i)
    return jsonify(json. dumps(plateno))

app.run(debug=True,host="0.0.0.0",port=5002)