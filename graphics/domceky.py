
import tkinter
from math import *

canvas = tkinter.Canvas(width=1100, height=600)
canvas.pack()
n = 8
x, y = 20, 150
a, z = 80, 100
canvas.create_line(-20,y+a, 1100, y+a, width=2)
canvas.create_line(-20,y+a+300, 1100,y+a+300, width=2)

for i in range(1,n+1):
    canvas.create_rectangle(x,y, x+a,y+a, fill="blue", tags="dom"+str(i))
    canvas.create_polygon(x-(z-a)/2,y, x-(z-a)/2+z,y, x-(z-a)/2+z/2,y-sqrt(-(z/2)**2+z**2), fill="red", tags="dom"+str(i))
    canvas.create_text(x+a/2, y+a/2, text=(i), fill="white", font="arial 20", tags="dom"+str(i))
    x += z
    
# prestahovat dom o ulicu dalej

n = int(input("Ktory dom prestahovat: "))
canvas.move("dom" + str(n), 0, 300)
tkinter.mainloop()

