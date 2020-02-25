from flask import Flask
from flask import request, jsonify , render_template
import markdown
import os
import time
import random
import cv2
import argparse
from detector import detection

app = Flask(__name__)


@app.route('/')
def index():
        with open("README.md", 'r') as markdown_file:
                content = markdown_file.read()
                return markdown.markdown(content)

@app.route('/getFreeSpaceToPark/', methods=['GET'])
def getFreeSpace():
    count=detection().detect()
    #count=random.randint(40,100)
    free_count=130-count
    if free_count>0:
        json_data= {"identifier"          : "FreeSpace",
                    "no of free spots"    : free_count,
                    "message"             :"success",
                    "time"                :time.ctime(),
                    "Entry Authentication":"OK"
                   }
        return jsonify(json_data), 201
    else:
        json_data= {"identifier"          : "FreeSpace",
                    "no of free spots"    : 0,
                    "message"             :"success",
                    "time"                :time.ctime(),
                    "Entry Authentication":"NOT OK"
                   }
        return jsonify(json_data), 201


app.run(debug=True,host="0.0.0.0",port=5001)



