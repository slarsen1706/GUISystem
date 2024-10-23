import json

def WriteJSON():
    meldinger = {}
    with open("meldinger", "r") as data:
        meldinger = data.load() 
        
    print(meldinger['avsender'])

WriteJSON() 
    
    