import tkinter

canvas = tkinter.Canvas(width=1000,height=600)
canvas.pack()

x, y = 500, 300
obr = tkinter.PhotoImage(file="pics/pyth.png")
canvas.create_image(x, y, image=obr)

tkinter.mainloop()

