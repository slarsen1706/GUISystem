import json
import os
import datetime

def CreateMessageObject(avsender: str, mottaker: str, melding: str):
    obj = {
        avsender : {
            mottaker:{
                datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S") : melding
            }
        }
    }
    
    return obj
    
def WriteJSON(message: object):
    meldinger = {}
    with open(os.getcwd() + "/meldinger.json", "r") as data:
        meldinger = json.loads(data.read())
    
    meldinger.update(message)
    
    
    with open(os.getcwd() + "/meldinger.json","w") as data:
        json.dump(meldinger, data)
        

