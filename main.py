from jsonHandler import *
from contacts import Contacts
from tkinter import *
import json

user = "Sander"
contacts = Contacts(user)
mottaker_chat = user

def endrePerson(btn):
    print(btn)
    person = btn
    print(f"endret person til {btn}")
    mottaker_chat = btn
    
def send():
    avsender = user
    mottaker = mottaker_chat
    melding = entry.get()
    message = CreateMessageObject(avsender, mottaker, melding)
    
    WriteJSON(message)
    
    print(f"Melding sendt fra {avsender} til {mottaker}.")

def motta(bruker1, bruker2):
    # Get the recipient's name from the user input
    mottaker = user
    messages = []
    try:
        # Load the messages from the JSON file
        with open("meldinger.json", "r") as fil:
            meldinger = json.load(fil)
    except FileNotFoundError:
        print("Ingen meldinger funnet.")
        return

    # Track if any messages for the recipient were found
    funnet = False

    # Iterate through all senders in the messages dictionary
    for avsender in meldinger:
        for mottaker in meldinger[avsender]:
            # Check if this sender has any messages for the recipient
            if mottaker in meldinger[avsender]:
                if (mottaker == bruker1 or mottaker == bruker2) and (avsender == bruker1 or avsender == bruker2):
                    for message in meldinger[avsender][mottaker]:
                        messages.append({message:{"from": avsender, "msg":meldinger[avsender][mottaker]}})
    return messages

def updateChat():
    # Clear canvaset
    for i in message_frame.children:
        i.destroy()
    
    # Legg til venner i friends_frame
    messages = motta(user, mottaker_chat)
    for i in range(len(messages)):  # Eksempel med 6 personer som i bildet
        key = list(messages[i].keys())[0]
        message = messages[i]
        Label(message_frame, text=message[key]['msg'], bg=("green" if messages[i][key]['from'] == user else "blue"), anchor="w").pack(anchor="w", padx=5)

          

# Opprette hovedvinduet
root = Tk()
root.title("Overføre GUI fra Drawio til tkinter")
root.config(bg="white")
root.geometry("400x400")

# Hovedframe
main_frame = Frame(root, bg="purple")
main_frame.pack(fill=BOTH, expand=True)

# Toppfelt med tittel og person
top_frame = Frame(main_frame, bg="pink", height=30)
top_frame.grid(row=0, column=1, sticky="nsew", columnspan=2)
top_frame.grid_columnconfigure(1, weight=1)
Label(top_frame, text="Program navn", bg="white", font=("Arial", 12)).grid(row=0, column=1)
Label(top_frame, text=user, bg="white").grid(row=0, column=2, padx=5)

# Venstre meny med venner-liste og scrollbar
left_frame = Frame(main_frame, bg="blue", width=100)
left_frame.grid(row=1, column=0, sticky="ns")
left_frame.grid_propagate(False)  # For å beholde bredde

# Canvas for å holde venner-listen
friends_canvas = Canvas(left_frame, bg="blue", width=100)
friends_canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar for vennelisten
scrollbar = Scrollbar(left_frame, orient="vertical", command=friends_canvas.yview)
scrollbar.pack(side=RIGHT, fill="y")
friends_canvas.configure(yscrollcommand=scrollbar.set)

# Inni canvas, lage en frame for venner-liste
friends_frame = Frame(friends_canvas, bg="white")
friends_canvas.create_window((0, 0), window=friends_frame, anchor="nw")

# Legg til venner i friends_frame
Label(friends_frame, text="Venner", bg="white", font=("Arial", 10, "bold")).pack(anchor="w")
venner = contacts.contacts
btns = []
for i in range(len(contacts.contacts)):  # Eksempel med 6 personer som i bildet
    btns.append(Button(friends_frame, text=venner[i], bg="white", anchor="w"))
    print(btns[-1])
    btns[-1].config(command=lambda j=i+1: endrePerson(venner[i]))
    btns[-1].pack(anchor="w", padx=5)

# Oppdatere scrollregionen til canvas
def configure_friends_canvas(event):
    friends_canvas.configure(scrollregion=friends_canvas.bbox("all"))

friends_frame.bind("<Configure>", configure_friends_canvas)

#Lag og oppdater chat vinduet

# Oppdatere scrollregionen til canvas

chat_frame = Frame(main_frame, bg="black", width=200, height=200)
chat_frame.grid(row=1, column=1, sticky="nsew", columnspan=2)
chat_frame.grid_rowconfigure(0, weight=1)
chat_frame.grid_columnconfigure(0, weight=1)

chat_canvas = Canvas(chat_frame, bg="blue", width=100)
chat_canvas.pack(side=LEFT, fill=BOTH, expand=True)
chat_canvas.create_window((0, 0), window=chat_frame, anchor="nw")

chat_scrollbar = Scrollbar(left_frame, orient="vertical", command=chat_canvas.yview)
chat_scrollbar.pack(side=RIGHT, fill="y")

message_frame = Frame(chat_frame, bg="black")
message_frame.pack()
def configure_friends_canvas(event):
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))

chat_frame.bind("<Configure>", configure_friends_canvas)

updateChat()

# Bunnfelt med input-boks og send-knapp
bottom_frame = Frame(main_frame, bg="white", height=30)
bottom_frame.grid(row=2, column=1, sticky="ew", columnspan=2)
Label(bottom_frame, text="Skriv inn her:", bg="white").pack(side=LEFT, padx=5)
entry = Entry(bottom_frame, width=30)
entry.pack(side=LEFT, padx=5)
Button(bottom_frame, text="Send", command=send).pack(side=RIGHT, padx=5)

# Layout-konfigurasjon
main_frame.grid_columnconfigure(0, weight=1)  # Venner-liste bredde
main_frame.grid_columnconfigure(1, weight=5)  # Chat-vinduet bredde
main_frame.grid_rowconfigure(1, weight=1)  # Chat-vinduet høyde

# Start hovedløkken
motta("Sander", "Idris")
root.mainloop()


