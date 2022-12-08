import tkinter
import random

canvas = tkinter.Canvas(height=500, width=800)
canvas.pack()


x, y = 50, 50
n = 10
sum = 0 

for i in range(n):
    hodnota = random.choice((1, 2, 5, 10, 20, 50))
    sum += hodnota
    canvas.create_rectangle(x,y, x+50, y+20, fill="white")
    canvas.create_text(x+25,y+10, text=str(hodnota)+"€")
    y += 20

x, y = 50, 50

canvas.create_text(x+100,y+30, text="spolu = "+str(sum)+"€", font="arial 12")

tkinter.mainloop()