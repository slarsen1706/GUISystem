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
    
    sender = message[message.keys[0]]
    receiver = sender[sender.keys[0]]
    if not message.keys[0] in meldinger:
        meldinger.Update(message)
    elif sender.keys[0] in meldinger[message.keys[0]]:
        meldinger[message.keys[0]].update(sender)
    else:
        meldinger[message.keys[0]][sender.keys[0]].update(receiver[receiver.keys[0]])
        
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
