from tkinter import *

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
Label(top_frame, text="Person", bg="white").grid(row=0, column=2, padx=5)

# Venstre meny med venner-liste og scrollbar
left_frame = Frame(main_frame, bg="blue", width=100)
left_frame.grid(row=1, column=0, sticky="ns")
left_frame.grid_propagate(False)  # For å beholde bredde

# Canvas for å holde venner-listen
canvas = Canvas(left_frame, bg="blue", width=100)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar for vennelisten
scrollbar = Scrollbar(left_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=RIGHT, fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Inni canvas, lage en frame for venner-liste
friends_frame = Frame(canvas, bg="white")
canvas.create_window((0, 0), window=friends_frame, anchor="nw")

# Legg til venner i friends_frame
Label(friends_frame, text="Venner", bg="white", font=("Arial", 10, "bold")).pack(anchor="w")
for i in range(1, 7):  # Eksempel med 6 personer som i bildet
    Label(friends_frame, text=f"Person {i}", bg="white", anchor="w").pack(anchor="w", padx=5)

# Oppdatere scrollregionen til canvas
def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

friends_frame.bind("<Configure>", configure_canvas)

# Chat-vinduet
chat_frame = Frame(main_frame, bg="black", width=200, height=200)
chat_frame.grid(row=1, column=1, sticky="nsew", columnspan=2)
chat_frame.grid_rowconfigure(0, weight=1)
chat_frame.grid_columnconfigure(0, weight=1)
Label(chat_frame, text="Chat", bg="black", fg="white", font=("Arial", 12)).place(relx=0.5, rely=0.5, anchor="center")

# Bunnfelt med input-boks og send-knapp
bottom_frame = Frame(main_frame, bg="white", height=30)
bottom_frame.grid(row=2, column=1, sticky="ew", columnspan=2)
Label(bottom_frame, text="Skriv inn her:", bg="white").pack(side=LEFT, padx=5)
entry = Entry(bottom_frame, width=30)
entry.pack(side=LEFT, padx=5)
Button(bottom_frame, text="Send").pack(side=RIGHT, padx=5)

# Layout-konfigurasjon
main_frame.grid_columnconfigure(0, weight=1)  # Venner-liste bredde
main_frame.grid_columnconfigure(1, weight=5)  # Chat-vinduet bredde
main_frame.grid_rowconfigure(1, weight=1)  # Chat-vinduet høyde

# Start hovedløkken
root.mainloop()
