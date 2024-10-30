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
    
def WriteMessageJSON(message: object):
    meldinger = {}
    with open(os.get_exec_path() + "/meldinger.json", "r") as data:
        meldinger = json.loads(data.read())
    
    meldinger.update(message)
    
    with open(os.get_exec_path() + "/meldinger.json","w") as data:
        json.dump(meldinger, data)

def FetchMessageJSON():
    meldinger = {}
    try:
        with open(os.get_exec_path() + "/meldinger.json", "r") as data:
            meldinger = json.loads(data.read())
    except:
        print("No message JSON found, skipping read")
    return meldinger