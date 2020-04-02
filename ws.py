# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:57:05 2020

@author: gangge
"""

from flask import Flask
from flask import request,make_response,jsonify
import numpy as np
from  datetime import datetime

import ai
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex = items[0]

app=Flask(__name__)
app.url_map.converters['reg'] = RegexConverter

@app.route("/status",methods=['GET'])
def status():
    result=jsonify({"Timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"version":'1.0'})
    return make_response(result)

@app.route("/predict",methods=['POST'])
def predict():
    
    data=request.get_data()
    if data is None:
        return make_response(jsonify({'error':'image can be None.'}))
    else:
        with open("imag.jpg",'wb') as f:
            f.write(data)    
        img = ai.image.load_img("imag.jpg", target_size=(224, 224))
        x = ai.image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = ai.preprocess_input(x)
        preds = ai.model.predict(x)
        # decode the results into a list of tuples (class, description, probability)
        # (one such list for each sample in the batch)
        predictResult=ai.decode_predictions(preds, top=3)[0]
        print('Predicted:', predictResult)
        result=jsonify({"result":predictResult})
        
        return make_response(result)

@app.route('/<reg(".+"):path>')
def other(path):
    return "api "+path+' not found!'

app.run()
