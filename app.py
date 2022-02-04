
'''
Created on 

Course work: 
    Flask REST API
@author: raja csp

Source:
    
'''

# Import necessary modules
from flask import Flask, render_template, request
import json

app = Flask(__name__)

'''
    Possible urls:
    http://0.0.0.0:5003/
'''
@app.route('/')
def start():

    result_dict = {
        'city' : 'Madurai', 
        'country' : 'Canada'
    }

    return result_dict

'''
    Possible urls:
    http://0.0.0.0:5003/get/user/info
'''
@app.route('/get/user/info')
def get_user_info():

    result_dict = {
        'name' : 'Kevin',
        'age' : '18'
    }

    return result_dict

'''
    Possible urls:
    http://0.0.0.0:5003/multiply?number=2

'''
@app.route('/multiply')
def do_multiply():

    # It should multiply by 6

    my_number = int(request.args['number'])

    result = 6 * my_number

    result_dict = {
        'result' : result,
        'my_number' : my_number
    }

    return result_dict

if __name__== "__main__":
    
    app.run(
        host = "0.0.0.0",  # localhost (127.0.0.1)
        debug = True, 
        port = 5003
    )
