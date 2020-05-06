# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:54:53 2020

@author: Pawan.Mishra
"""

from flask import Flask,request,jsonify
import pandas as pd
import os
from flask_cors import CORS, cross_origin
path = os.getcwd()
app = Flask(__name__)
path = os.getcwd()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/TradeInOptions", methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def TradeInOptions():  
    TradeList= []
    tradeInOptions = pd.read_csv(path+"\\"+"TradeOptions.csv")
    tradeIn = tradeInOptions["TradeOptions"]  
    for trade in tradeIn:
        TradeList.append(trade)
    return jsonify({"OptionType": tradeInOptions["OptionType"][0],"Options": TradeList,"textMessage": tradeInOptions["textMessage"][0]})


@app.route('/Manufacture', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def Manufacture():
        text_data = request.form.get("data")
        ManufactureOptions = pd.read_csv(path+"\\"+"TradeManufacture.csv")        
        if text_data == "TradeIn":
            Manufacture = ManufactureOptions["ManufactureName"]  
            ManufactureList = [x for x in Manufacture if str(x) != 'nan']
            return jsonify({"OptionType": ManufactureOptions["OptionType"][0],"Options": ManufactureList,"textMessage": ManufactureOptions["textMessage"][0]})
        elif text_data == "Upgrade": # No Data given for upgrade
            return jsonify({"OptionType": ManufactureOptions["OptionType"][0],"Options": ManufactureList,"textMessage": ManufactureOptions["textMessage"][0]})
        
        else:
            return jsonify("Please select the correct Manufacture Name")
        
@app.route('/Model', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def Model():
        text_data = request.form.get("data")
        ModelOptions = pd.read_csv(path+"\\"+"TradeModel.csv")        
        if text_data == "Apple":
            Model = ModelOptions["ModelNameApple"]  
            ModelList = [x for x in Model if str(x) != 'nan']
            return jsonify({"OptionType": ModelOptions["OptionType"][0],"Options": ModelList,"textMessage": ModelOptions["textMessage"][0]})
        elif text_data == "Google": 
            Model = ModelOptions["ModelNameGoogle"]  
            ModelList = [x for x in Model if str(x) != 'nan']          
            return jsonify({"OptionType": ModelOptions["OptionType"][0],"Options": ModelList,"textMessage": ModelOptions["textMessage"][0]})
        elif text_data == "Samsung": 
            Model = ModelOptions["ModelNameSamsung"]  
            ModelList = [x for x in Model if str(x) != 'nan']
            return jsonify({"OptionType": ModelOptions["OptionType"][0],"Options": ModelList,"textMessage": ModelOptions["textMessage"][0]})
        elif text_data == "Others": # No Data given for Others         
            return jsonify({"OptionType": ModelOptions["OptionType"][0],"Options": ModelList,"textMessage": ModelOptions["textMessage"][0]})
              
        else:
            return jsonify("Please select the correct Model Name")        

@app.route('/Memory', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def Memory():
        text_data = request.form.get("data")
        MemoryOptions = pd.read_csv(path+"\\"+"TradeMemory.csv") 
        ModelOptions = pd.read_csv(path+"\\"+"TradeModel.csv")
        Model = ModelOptions["ModelNameApple"] 
        Model=Model.append(ModelOptions["ModelNameSamsung"])
        Model=Model.append(ModelOptions["ModelNameGoogle"])
        ModelList = [x for x in Model if str(x) != 'nan']
        print(ModelList)
        if text_data in ModelList:
            Memory = MemoryOptions["Memorytype"]  
            MemoryList = [x for x in Memory if str(x) != 'nan']
            return jsonify({"OptionType": MemoryOptions["OptionType"][0],"Options": MemoryList,"textMessage": MemoryOptions["textMessage"][0]})
        else:
            return jsonify("Please select the correct Memory type")






app.run(host='0.0.0.0',port=8000,debug=True)# change IP as per the hosting machine 