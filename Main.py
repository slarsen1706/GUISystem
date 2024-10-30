from jsonHandler import *
import json

def send():
    avsender = input("Avsender: ").lower()
    mottaker = input("Mottaker: ").lower()
    melding = input("Meldingen: ").lower()

    
    message = CreateMessageObject(avsender, mottaker, melding)
    
    WriteJSON(message)
    
    print(f"Melding sendt fra {avsender} til {mottaker}.")

def motta():
    # Get the recipient's name from the user input
    mottaker = input("Skriv inn navnet ditt for å sjekke meldinger: ").lower()

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
        # Check if this sender has any messages for the recipient
        if mottaker in meldinger[avsender]:
            funnet = True
            # Print each message sent to the recipient
            for tidsstempel, melding in meldinger[avsender][mottaker].items():
                print("")
                print(f"Fra: {avsender}, Kl: {tidsstempel}, Melding: {melding}")
                print("")

    # Inform the user if no messages were found for the recipient
    if not funnet:
        print(f"Ingen meldinger for {mottaker}.")

def main():
    while True:
        handling = input("Send en melding (s) eller sjekk meldinger (r)? (q for å avslutte): ").lower()
        if handling == 's':
            send()
        elif handling == 'r':
            motta()
        elif handling == 'q':
            break
main()
