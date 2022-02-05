
'''
Created on 

Course work: 
    Flask REST API
@author: raja csp

Source:
    
'''

# Import necessary modules
from flask import Flask, render_template, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

'''
    Possible urls:
    http://0.0.0.0:5003/
'''


@app.route('/')
def start():

    f = open('result1.json', "r")
    
    # Reading from file
    data = json.loads(f.read())


    # result_dict = {
    #     'city' : 'Madurai', 
    #     'country' : 'india'
    # }
    
    return jsonify(data)

if __name__== "__main__":
    
    app.run(
        host = "0.0.0.0",  # localhost (127.0.0.1)
        debug = True, 
        port = 5003
    )
