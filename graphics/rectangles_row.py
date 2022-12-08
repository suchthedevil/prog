import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

y = 200

farba1, farba2 = "red", "blue"
for x in range(10,490,30):
    canvas.create_rectangle(x,y,x+25,y+100, fill=farba1)
    farba1, farba2 = farba2, farba1

tkinter.mainloop()
