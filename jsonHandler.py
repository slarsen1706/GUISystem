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
    
    sender = list(message.keys())[0]
    receiver = list(message[sender].keys())[0]
    if not sender in meldinger:
        meldinger.update(message)
    elif not receiver in meldinger[sender]:
        meldinger[sender].update(message[sender])
    else:
        meldinger[sender][receiver].update(message[sender][receiver])
        
    with open(os.getcwd() + "/meldinger.json","w") as data:
        json.dump(meldinger, data)

def FetchMessageJSON():
    meldinger = {}
    try:
        with open(os.getcwd() + "/meldinger.json", "r") as data:
            meldinger = json.loads(data.read())
    except:
        print("No message JSON found, skipping read")
    return meldinger
