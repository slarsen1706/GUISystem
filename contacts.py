from jsonHandler import *

class Contacts(object):
    def __init__(self, user):
        messages = FetchMessageJSON()
        self.contacts = []
        for sender in messages:
            for receiver in messages[sender]:
                if (sender in self.contacts) or (receiver in self.contacts):
                    continue
                if receiver == user or sender == user:
                    self.contacts.append(receiver)
                    
    def UpdateContact(self):
        self.__init__()