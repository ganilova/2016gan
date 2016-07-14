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
# x=button['text']='Новый заголовок'

def init_main_window():#Инициализация главного окна
    global root, button1, button2,label, text, scale
    root = Tk()
    button1 = Button(root, text="Button_1",command=button1_command)#Срабатывает на нажатие и отпуск мышки
    button1.bind("<Button>", print_hello)# Срабатывает на клик мышки
    button1.pack()

    button2 = Button(root, text="Button_2")
    button2.bind("<Button>", print_hello)
    button2.pack()
    variable = IntVar()
    #label = Label(root, text='Some text.')
    label = Label(root, textvariable=variable)#привязка к переменной
    scale =Scale(root, orient=HORIZONTAL,length=300,
          from_=0,to=100,tickinterval=10,resolution=1, variable=variable)
    text = Entry(root, textvariable=variable)
    label.pack()
    scale.pack()
    text.pack()

if __name__ == '__main__':
    init_main_window()

    root.mainloop()