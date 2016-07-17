from tkinter import*
from random import choice, randint

ball_min = 15
ball_max = 40
ball_color = '0123456789ABCDEF'
balls_coord = []#список координат шариков
balls_num = []#список номеров шариков

def click_ball(event):
    """ удаление шарика по клику мышки
    подсчет удаленных шариков """
    global points, label_bonus, balls_coord, balls_num
    obj = canvas.find_closest(event.x, event.y)
    num = obj[0]# вытаскиваем номер объекта из кортежа
    x1, y1, x2, y2 =canvas.coords(obj)
    if x1 < event.x < x2 and y1 < event.y < y2:
        index = balls_num.index(num)# определяем индекс элемента списка, где храниться номер объекта
        balls_num.pop(index)# удаляем элемент списка с номером объекта
        balls_coord.pop(index)# удаляем элемент списка с координатами объекта
        canvas.delete(obj)
        points+=1
        label_bonus['text']=points # изменяем надпись на метке (число удаленных шаров)
        create_random_ball()

def move_all_balls(event):#Передвигает все шарики
    global balls_coord
    for obj in balls_coord:
        x1, y1, x2, y2 =canvas.coords(obj[0])
        # проверяем, не выйдет ли шарик за границы холста
        if x1+obj[1]+obj[3]>=400 or x1+obj[1]<=0:
            obj[1]=-obj[1] #меняем направление движения
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
    color = '#'
    for c in range(6):
        color = color + choice(ball_color)
    return color

def init_balls(event): # Создает начальные шарики для игры
    let = input_balls.get()
    if let != '':
        ball_count = int(let)
    else:
        ball_count = 0
    for i in range(ball_count):
        create_random_ball()
        input_balls.destroy()
        input_text.destroy()

def init_main_window():
    global root, canvas, label_bonus, points, frame_text, frame_canvas, input_balls, input_text
    root = Tk()
    frame_text = Frame(root)
    input_balls = Entry(frame_text,width=5, font="12")
    input_text = Label(frame_text, text = 'Введите число шариков', width=20, font='Calibri 14')
    input_balls.grid(row=0, column=1)
    input_text.grid(row=0, column=0)
    label_text = Label(frame_text, text = 'Набранные очки', width=20, font='Calibri 14')
    label_bonus = Label(frame_text, text='0', font='Calibri 14')
    label_text.grid(row=1, column=0)
    label_bonus.grid(row=1, column=1)
    frame_text.pack()
    input_balls.focus_set()
    input_balls.bind("<Return>",init_balls)
    points = 0 # число удаленных шариков
    frame_canvas = Frame(root)
    frame_canvas.pack()
    canvas = Canvas(frame_canvas, background="white", width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()

if __name__ == '__main__':
    init_main_window()
    #init_balls()
    root.mainloop()
