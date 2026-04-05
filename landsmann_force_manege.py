from tkinter import *


fenetre_principale = Tk()
fenetre_principale.title("TP Manège Parc d'attraction - BTS CIEL")
fenetre_principale.geometry("450x300")
label=Label(fenetre_principale, text="Manege du parc - Force 1 / Force 2", fg="navy", font="18")
label.pack()
label=Label(fenetre_principale, text="Entrez votre âge et votre taille pour savoir à quelle force vous pouvez faire le manège.", wraplength=400, pady=10)
label.pack()
label=Label(fenetre_principale, text="Entrez votre âge : ")
label.pack()
age=Entry(fenetre_principale, width=10)
age.pack(pady=10)
label=Label(fenetre_principale, text="Entrez votre taille en mètres : ")
label.pack()
taille=Entry(fenetre_principale, width=10)
taille.pack(pady=10)
def affiche_message():
    if (age.get() =='' or taille.get() == ''):
        champs_non_remplis()
    elif type(int(age.get())) == str or type(float(taille.get())) == str:
        champs_remplis_lettres()
    else:
        manege_autorise()
def champs_non_remplis():
    champs_non_remplis=Label(fenetre_principale,text="Erreur : tous les champs ne sont pas remplis",fg="red")
    champs_non_remplis.pack()
def champs_remplis_lettres():
    champs_remplis_lettres=Label(fenetre_principale,text="Erreur : les lettres ne sont pas acceptées",fg="red")
    champs_remplis_lettres.pack()
def manege_autorise():
    if float(taille.get()) < 1.1:
        manege_non_autorise=Label(fenetre_principale,text="Erreur : taille insuffisante",fg="red")
        manege_non_autorise.pack()
    if float(taille.get()) >= 1.1 and float(taille.get()) < 1.6:
        manege_force_1=Label(fenetre_principale,text="Manège autorise en force 1",fg="blue")
        manege_force_1.pack()
    if float(taille.get()) >= 1.6:
        manege_force_2=Label(fenetre_principale,text="Manège autorise en force 2",fg="blue")
        manege_force_2.pack()
envoyer=Button(fenetre_principale, text="Envoyer", command=affiche_message)
envoyer.pack(pady=10)
fenetre_principale.mainloop()