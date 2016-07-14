from tkinter import*
from random import choice, randint
ball_count = 20
ball_min = 15
ball_max = 40
ball_color = ['green', 'lightgrey', 'red', 'yellow', 'blue', 'lightgreen', 'lightblue', '#AA00FF']
global points
def click_ball(event):
    """ удаление шарика по клику мышки
    подсчет удаленных шариков """
    global points, label, root
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 =canvas.coords(obj)
    if x1<event.x < x2 and y1<event.y< y2:
        canvas.delete(obj)
        points+=1
        label['text']=points
        create_random_ball()

def move_all_balls(event):#Передвигает все шарики
    for obj in canvas.find_all():
        dx = randint(-5, 5)
        dy = randint(-5, 5)
        canvas.move(obj, dx, dy)


def create_random_ball(): #Создание шарика в случайном месте игрового поля
    R = randint(ball_min, ball_max)
    x = randint(R,int(canvas['width'])-R)
    y = randint(R,int(canvas['height'])-R)
    canvas.create_oval(x, y, x+R, y+R, width=0, fill=random_color())

def random_color():
    """
    :return: Цвет шарика
    """
    return choice(ball_color)

def init_ball(): # Создает шарики для игры
    for i in range(ball_count):
        create_random_ball()

def init_main_window():
    global root, canvas, label, points
    root = Tk()
    label_text = Label(root, text = 'Набранные очки')
    label_text.pack()
    points = 0
    label = Label(root, text=points)#привязка к переменной
    label.pack()
    canvas = Canvas(root, background="white", width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()

if __name__ == '__main__':
    init_main_window()
    init_ball()
    root.mainloop()
