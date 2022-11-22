from tkinter import *
import threading


def tester():
    global color
    if color != '':
        if color == 'green':
            greenlight()
        elif color == 'yellow':
            yellowlight()
        elif color == 'red':
            redlight()
        # pour récuperer le temps selectionée dans le listbox
        # (par default c'est la première valeur du listbox = 1)
        # et ré-exécuter la fonction 'tester' après ce temps
        timer = threading.Timer(int(list_time.get(ACTIVE)), tester)
        timer.start()
    else:
        color = 'green'


def quitter():
    global color
    # pour supprimer la valeur de la variable color
    color = ''
    # pour rendre les couleurs de début
    rightc.itemconfig(green, fill="#D5F5E3")
    rightc.itemconfig(yellow, fill="#FCF3CF")
    rightc.itemconfig(red, fill="#F2D7D5")


def greenlight():
    # pour rendre la variable color globale
    global color
    # pour changer la couleur du cercle vert
    rightc.itemconfig(green, fill="green")
    rightc.itemconfig(yellow, fill="#FCF3CF")
    rightc.itemconfig(red, fill="#F2D7D5")
    # pour déclarer la prochaine couleur 'jaune'
    color = 'yellow'


def yellowlight():
    # pour rendre la variable color globale
    global color
    # pour changer la couleur du cercle jaune
    rightc.itemconfig(green, fill="#D5F5E3")
    rightc.itemconfig(yellow, fill="yellow")
    rightc.itemconfig(red, fill="#F2D7D5")
    # pour déclarer la prochaine couleur 'rouge'
    color = 'red'


def redlight():
    # pour rendre la variable color globale
    global color
    # pour changer la couleur du cercle rouge
    rightc.itemconfig(green, fill="#D5F5E3")
    rightc.itemconfig(yellow, fill="#FCF3CF")
    rightc.itemconfig(red, fill="red")
    # pour déclarer la prochaine couleur 'vert'
    color = 'green'


fenetre = Tk()

# info sur la fenetre
fenetre.title("Traffic lights")
fenetre.geometry('700x500')
fenetre.resizable(False, False)
title = Label(fenetre, text='Traffic lights', fg='white', bg='#1e3d59')
title.config(font=('times', 20, 'bold'))
title.pack(fill=X)

# pour initialiser la couleur à la couleur vert
color = 'green'

# canvas à gauche
# pour créer le canvas des temps
leftc = Canvas(fenetre, width=350, height=660, bg='#f5f0e1')
leftc.place(x=0, y=37)
# pour créer le listbox des temps 'list_time'
list_time = Listbox(fenetre, width=20, height=10)
list_time.place(x=100, y=180)
# les temps à remplir dans le listbox
times = ['1', '5', '25', '50', '75', '100', '150', '200', '250', '300']
for i in times:
    # pour remplir le listbox
    list_time.insert(END, i)


# canvas à droite
# pour créer le canvas des couleurs
rightc = Canvas(fenetre, width=350, height=660, bg='#f5f0e1')
rightc.place(x=346, y=37)
# pour créer un rectangle
rightc.create_rectangle(100, 90, 180, 350, width=3)
# pour créer les cercles colorés
green = rightc.create_oval(110, 100, 170, 160, width=3, fill='#D5F5E3')
yellow = rightc.create_oval(110, 190, 170, 250, width=3, fill='#FCF3CF')
red = rightc.create_oval(110, 280, 170, 340, width=3, fill='#F2D7D5')

# les bouttons
# pour créer un boutton "tester" dans le canvas à droite
btn = Button(rightc, text='TESTER ', command=tester,
             fg='#f5f0e1', bg='#1e3d59')
btn.config(font=('times', 16, 'bold'))
btn.place(x=200, y=100)
# pour créer un boutton "quitter" dans le canvas à droite
btn = Button(rightc, text='QUITTER', command=quitter,
             fg='#f5f0e1', bg='#1e3d59')
btn.config(font=('times', 16, 'bold'))
btn.place(x=200, y=180)

fenetre.mainloop()
