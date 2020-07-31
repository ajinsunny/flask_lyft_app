
#Library Imports
import os
from flask import Flask, abort, request,jsonify,json


#Initiate the application instance
app = Flask(__name__)

#Route to (./test) to make the POST request 

@app.route('/test', methods=['GET','POST'])
def test():
    string_to_cut = request.json['string_to_cut']
    result_string = string_parser(string_to_cut)
    json_obj = {
        "return_string": result_string,
    }
    return json.dumps(json_obj)
    
def string_parser(string):
    result_string = []
    for i in range(2,len(string),3):
            result_string.append(string[i])
    return "".join(result_string)




    
