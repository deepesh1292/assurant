# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:46:09 2020

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


@app.route('/assurent', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def TradeIn():  
        
        text_data = request.form.get("data")
        ModelList=[]        
        ManufactureList=[]
        tradeInList=[]
        TradeList =[]
        UpdateList=[]
        tradeInOptions = pd.read_csv(path+"\\"+"TradeOptions.csv")
        tradeIn = tradeInOptions["TradeOptions"]  
        tradeInList = [x for x in tradeIn if str(x) != 'nan']
        
        ManufactureOptions = pd.read_csv(path+"\\"+"TradeManufacture.csv")  
        Manufacture = ManufactureOptions["ManufactureName"]  
        ManufactureList = [x for x in Manufacture if str(x) != 'nan']        
        
        ModelOptions = pd.read_csv(path+"\\"+"TradeModel.csv",encoding= 'unicode_escape')
        Model = ModelOptions["ModelNameApple"] 
        Model=Model.append(ModelOptions["ModelNameSamsung"])
        Model=Model.append(ModelOptions["ModelNameGoogle"])
        ModelList = [x for x in Model if str(x) != 'nan']
        
        MemoryOptions = pd.read_csv(path+"\\"+"TradeMemory.csv",encoding= 'unicode_escape')            
        Memory = MemoryOptions["Memorytype"]  
        MemoryList = [x for x in Memory if str(x) != 'nan'] 
        
        if text_data=='home' and request.method == 'POST':    
            
            tradeInOptions = pd.read_csv(path+"\\"+"TradeOptions.csv")
            tradeIn = tradeInOptions["TradeOptions"]  
            for trade in tradeIn:
                TradeList.append(trade)
            return jsonify([{"OptionType": tradeInOptions["OptionType"][0],"Options": TradeList,"textMessage": tradeInOptions["textMessage"][0]}])

        elif text_data in tradeInList and request.method == 'POST':
            print(tradeInList)
            if text_data == "TradeIn":                
                return jsonify([{"OptionType": ManufactureOptions["OptionType"][0],"Options": ManufactureList,"textMessage": ManufactureOptions["textMessage"][0]}])
            elif text_data == "Upgrade": # No Data given for upgrade
                return jsonify([{"OptionType": ManufactureOptions["OptionType"][0],"Options": UpdateList,"textMessage": ManufactureOptions["textMessage"][0]}])

# Manufacture
      
        elif text_data in ManufactureList and request.method == 'POST':
            print(ManufactureList)
            ModelList_others=["Xiaomi","NOKIA","MOTOROLA"]
            if text_data == "Apple":
                Model_apple = ModelOptions["ModelNameApple"]  
                Model_appleList = [x for x in Model_apple if str(x) != 'nan']
                return jsonify([{"OptionType": ModelOptions["OptionType"][0],"Options": Model_appleList,"textMessage": ModelOptions["textMessage"][0]+" for "+text_data+" brand "}])
            elif text_data == "Google": 
                Model_Google = ModelOptions["ModelNameGoogle"]  
                Model_GoogleList = [x for x in Model_Google if str(x) != 'nan']
                return jsonify([{"OptionType": ModelOptions["OptionType"][0],"Options": Model_GoogleList,"textMessage": ModelOptions["textMessage"][0]+" for "+text_data+" brand "}])
            elif text_data == "Samsung": 
                Model_Samsung = ModelOptions["ModelNameSamsung"]  
                Model_SamsungList = [x for x in Model_Samsung if str(x) != 'nan']
                return jsonify([{"OptionType": ModelOptions["OptionType"][0],"Options": Model_SamsungList,"textMessage": ModelOptions["textMessage"][0]+" for "+text_data+" brand "}])
            elif text_data == "Others": # No Data given for Others         
                return jsonify([{"OptionType": ModelOptions["OptionType"][0],"Options": ModelList_others,"textMessage": ModelOptions["textMessage"][0]+" for "+text_data+" brand "}])

# Model
                
        elif text_data in ModelList  and request.method == 'POST':  
            print(ModelList)
            if text_data in ModelList:
                Memory = MemoryOptions["Memorytype"]  
                MemoryList = [x for x in Memory if str(x) != 'nan']
                return jsonify([{"OptionType": MemoryOptions["OptionType"][0],"Options": MemoryList,"textMessage": MemoryOptions["textMessage"][0]+" for model "+text_data}])

#Memory
            
        elif text_data in MemoryList and request.method == 'POST':  
            if text_data in MemoryList:
                return jsonify([ {"textMessage": "Enter the IMEI number","OptionType": "textBox","Options": ["Submit"]}])
# accept/reject
                
        elif text_data == 'submit' and request.method == 'POST':
                return jsonify([{
                "textMessage": "Your Offer value is : $500",
                "Options": [
                  "Accept",
                  "Reject"
                ],
                "OptionType": "Button"
              }])
    
        elif text_data in["Accept","Reject"] and request.method == 'POST':
            if text_data == "Accept":
                return jsonify([{"OptionType": "Info","textMessage": "Your offer was accepted"}])
            elif text_data == "Reject":
                return jsonify([{"OptionType": "Info","textMessage": "Your offer was rejected"}])
# Device Condition      
        elif text_data and request.method == 'POST': 
             
            DeviceCondition = pd.read_csv(path+"\\"+"TradeDeviceCondition.csv")
            Condition = DeviceCondition["textMessage"]  
            ConditionListMsg = [x for x in Condition if str(x) != 'nan']
            ConditionOptionType = DeviceCondition["OptionType"]  
            ConditionOptionTypeList = [x for x in ConditionOptionType if str(x) != 'nan']
            ConditionradioOptions = DeviceCondition["radioOptions"]  
            ConditionradioOptionsList = [x for x in ConditionradioOptions if str(x) != 'nan']
            Options = DeviceCondition["Options"]  
            OptionsList = [x for x in Options if str(x) != 'nan']
            return jsonify([{"OptionType": ConditionOptionTypeList[0],"Options":OptionsList,"radioOptions": ConditionradioOptionsList,"textMessage": ConditionListMsg[0]},{"OptionType": ConditionOptionTypeList[1],"Options":OptionsList,"radioOptions": ConditionradioOptionsList,"textMessage": ConditionListMsg[1]},{"OptionType": ConditionOptionTypeList[2],"Options":OptionsList,"radioOptions": ConditionradioOptionsList,"textMessage": ConditionListMsg[2]}])

        else:
            return jsonify("Please select the correct values")
        
        
#app.run(host='0.0.0.0',port=8000,debug=True)# change IP as per the hosting machine 