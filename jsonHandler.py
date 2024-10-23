import json
import os

def WriteJSON():
    meldinger = {}
    with open(os.getcwd() + "/meldinger.json", "r") as data:
        meldinger = json.loads(data.read())
    
    nyttObj = {"Sander":{"Asrom":{"Tidspunktet":"Meldingen"}}}
    meldinger.update(nyttObj)
    
    
    with open(os.getcwd() + "/meldinger.json","w") as data:
        json.dump(meldinger, data)
        

WriteJSON() 
    
    