import tkinter as tk
from contacts import Contacts
from scrollableFrame import ScrollableFrame

contacts = Contacts("Sander")
WIDTH = 300
HEIGHT = 150
root = tk.Tk()

root.minsize(WIDTH, HEIGHT)

option = contacts.contacts
value = tk.StringVar(root)
value.set(option[0])

dropdown = tk.OptionMenu(root, value, *option)
title = tk.Label(root, text="Chat", width=int(WIDTH/2), justify="center")
userLabel = tk.Label(root, text="Sander", justify="center")

chatFrame = ScrollableFrame(root, width=WIDTH)

dropdown.pack(padx=5, pady=5)
title.pack(padx=5, pady=5)
userLabel.pack(padx=5, pady=5)
chatFrame.pack(padx=5, pady=5)

root.mainloop()
