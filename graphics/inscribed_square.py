import tkinter

canvas = tkinter.Canvas(height=500,width=800)
canvas.pack()

x,y = 400, 250
r = 100 
canvas.create_oval(x+100,y+100,x-100,y-100)
canvas.create_rectangle(x+100,y+100,x-100,y-100)

canvas.create_line(x-r, y, x, y+r, x+r, y, x, y-r, x-r, y,)
canvas.create_polygon(x-r, y, x, y+r, x+r, y, x, y-r, fill="")
tkinter.mainloop()

#utvar sa neda otocit potom ako je nakresleny,
#treba nakreslit novy utvar



