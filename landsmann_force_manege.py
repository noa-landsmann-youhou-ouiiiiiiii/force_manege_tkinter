from tkinter import *

print("test")

fenetre = Tk()
fenetre.title("TP Manège Parc d'attraction - BTS CIEL")
fenetre.geometry("450x300")
label=Label(fenetre, text="Manege du parc - Force 1 / Force 2",fg="navy",font="18")
label.pack()
label=Label(fenetre, text="Entrez votre âge et votre taille pour savoir à quelle force vous pouvez faire le manège.",wraplength=400,pady=10)
label.pack()
label=Label(fenetre, text="Entrez votre âge : ")
label.pack()
age=Entry(fenetre, width=10)
age.pack()
fenetre.mainloop()