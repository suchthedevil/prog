"""
import tkinter

canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 30, 190, 110)

tkinter.mainloop()
"""
#VYHODNEJSI ZAPIS, pouzivat toto:

import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x, y = 50, 30
sirka, vyska = 140, 80
canvas.create_rectangle(x, y, x + sirka, y + vyska)

tkinter.mainloop()


#Nakreslíme 10 rovnako veľkých obdĺžnikov na náhodné pozície:

import tkinter
import random

canvas = tkinter.Canvas(width=800, height=500)
canvas.pack()

for i in range(10):
    x = random.randint(10, 600)
    y = random.randint(10, 300)
    sirka, vyska = 140, 80
    canvas.create_rectangle(x, y, x + sirka, y + vyska, fill="red")

tkinter.mainloop()

