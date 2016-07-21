from tkinter import*


def paint(event):
    canvas.coords(line, 0, 0, event.x, event.y)



root = Tk()

canvas = Canvas(root, background="white", width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0, 0, 10, 10)
for i in range(10):
    oval = canvas.create_oval(i*40, i*40, i*40+30, i*40+30, fill='lightgreen', outline='red')


root.mainloop()
print('Exit')