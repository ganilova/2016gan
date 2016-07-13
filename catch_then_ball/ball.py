from tkinter import*
def button1_command():
    print("Button 1 default command")
def print_hello(event):
    print(event.num)
    print(event.x, event.y)
    me=event.widget
    if me==button1:
        print("Hello!")
    elif me==button2:
        print("You pressed button 2")
    else:
        raise ValueError()

root = Tk()
button1 = Button(root, text="Button_1",command=button1_command)#Срабатывает на нажатие и отпуск мышки
button1.bind("<Button>", print_hello)# Срабатывает на клик мышки
button1.pack()
button2 = Button(root, text="Button_2")
button2.bind("<Button>", print_hello)
button2.pack()


root.mainloop()