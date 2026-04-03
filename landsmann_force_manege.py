from tkinter import *

print("test")

fenetre = Tk()
fenetre.title("TP Manège Parc d'attraction - BTS CIEL")
fenetre.geometry("450x300")
label=Label(fenetre, text="Manege du parc - Force 1 / Force 2",bg="yellow")
label.pack(side="bottom",fill="x")
fenetre.mainloop()