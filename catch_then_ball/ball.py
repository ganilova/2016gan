from tkinter import*
from random import choice, randint

ball_count = 20
ball_min = 15
ball_max = 40
ball_color = ['green', 'lightgrey', 'red', 'yellow', 'blue', 'lightgreen', 'lightblue', '#AA00FF']
balls_coord = []#список координат шариков
balls_num = []#список номеров шариков

def click_ball(event):
    """ удаление шарика по клику мышки
    подсчет удаленных шариков """
    global points, label, balls_coord, balls_num
    obj = canvas.find_closest(event.x, event.y)
    num = obj[0]# вытаскиваем номер объекта из кортежа
    x1, y1, x2, y2 =canvas.coords(obj)
    if x1 < event.x < x2 and y1 < event.y < y2:
        canvas.delete(obj)
        index = balls_num.index(num)# определяем индекс элемента списка, где храниться номер объекта
        balls_num.pop(index)# удаляем элемент списка с номером объекта
        balls_coord.pop(index)# удаляем элемент списка с координатами объекта
        points+=1
        label['text']=points # изменяем надпись на метке (число удаленных шаров)
        create_random_ball()

def move_all_balls(event):#Передвигает все шарики
    global balls_coord
    for obj in balls_coord:
        x1, y1, x2, y2 =canvas.coords(obj[0])
        if x1+obj[1]+obj[3]>=400 or x1+obj[1]<=0:
            obj[1]=-obj[1]
        if y1+obj[2]+obj[3]>=400 or y1+obj[2]<=0:
            obj[2]=-obj[2]
        canvas.move(obj[0],obj[1],obj[2])


def create_random_ball(): #Создание шарика в случайном месте игрового поля
    global balls_coord, balls_num
    R = randint(ball_min, ball_max)
    x = randint(R,int(canvas['width'])-R)
    y = randint(R,int(canvas['height'])-R)
    #рисуем шарик и запоминаем его номер в num_oval
    num_oval = canvas.create_oval(x, y, x+R, y+R, width=0, fill=random_color())
    dx = randint(-2, 2)
    dy = randint(-2, 2)
    # запоминаем идентификатор, вектор и радиус движения нового шарика
    balls_coord.append([num_oval, dx, dy, R])
    balls_num.append(num_oval)# запоминаем номер нового шарика


def random_color():
    return choice(ball_color)

def init_balls(): # Создает начальные шарики для игры
    for i in range(ball_count):
        create_random_ball()

def init_main_window():
    global root, canvas, label, points
    root = Tk()
    label_text = Label(root, text = 'Набранные очки')
    label_text.pack()
    points = 0 # число удаленных шариков
    label = Label(root, text=points)
    label.pack()
    canvas = Canvas(root, background="white", width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()

if __name__ == '__main__':
    init_main_window()
    init_balls()
    root.mainloop()
