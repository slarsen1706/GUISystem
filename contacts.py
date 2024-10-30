from jsonHandler import *

class Contacts(object):
    def __init__(self, user):
        #Get the messages stored in the JSON file
        messages = FetchMessageJSON()
        self.contacts = []
        #Loop over all the messages, if they are from/to the user, then they are added to the contacts
        for sender in messages:
            for receiver in messages[sender]:
                #If the person is already in the contacts, skip them
                if (sender in self.contacts) or (receiver in self.contacts):
                    continue
                #If either the sender or receiver is the user, add them in the contacts
                if receiver == user or sender == user:
                    self.contacts.append(receiver)
                    
    def UpdateContact(self):
        self.__init__()