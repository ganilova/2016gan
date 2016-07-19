from tkinter import*
from random import choice, randint
import time

ball_min = 15
ball_max = 40
ball_color = '0123456789ABCDEF'
balls_coord = []#список координат шариков
balls_num = []#список номеров шариков
time_limit = 10
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
    if time2>0:
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
    global timeEnd
    let = input_balls.get()
    if let != '':
        ball_count = int(let)
        for i in range(ball_count):
            create_random_ball()
            input_balls.destroy()
            input_text['text']='Шариков на поле'
            label = Label(frame_text, text=let, font='Calibri 14')
            label.grid(row=0, column=1)
        timeEnd = int(time.time()+time_limit)
        tick()


def close_win():
    root.destroy()

def close_rule():
    tex.destroy()
    close.destroy()
    win.destroy()

def new_win():
    global win, tex, close
    win = Toplevel(root)
    win.title("Правила игры")
    rule = "За отведенное время надо набрать\n наибольшее количество очков"
    tex = Label(win, text=rule, width=40,height= 10, font="Verdana 12")
    tex.pack()
    close = Button(win, text="Закрыть",command=close_rule)#Срабатывает на нажатие и отпуск мышки
    close.pack()

def init_menu():
    m = Menu(root)
    root.config(menu = m)
    fm = Menu(m)
    m.add_cascade(label="Меню", menu=fm)
    fm.add_command(label="Правила игры", command=new_win)
    fm.add_command(label="Выход", command=close_win)

def tick():
    global timeEnd, time2
    time2 = timeEnd - int(time.time())
    if time2 >=0:
        time_Go.config(text=time2)
        time_Go.after(200, tick)

def init_main_window():
    global root,time_Go, canvas, label_bonus, points, frame_text, frame_canvas, input_balls, input_text
    root = Tk()
    init_menu()
    frame_text = Frame(root)
    frame_text.pack()
    input_balls = Entry(frame_text,width=5, font="12")
    input_text = Label(frame_text, text = 'Введите число шариков', width=20, font='Calibri 14')
    input_balls.grid(row=0, column=1)
    input_text.grid(row=0, column=0)
    label_text = Label(frame_text, text = 'Набранные очки', width=20, font='Calibri 14')
    label_bonus = Label(frame_text, text='0', font='Calibri 14')
    label_text.grid(row=1, column=0)
    label_bonus.grid(row=1, column=1)
    input_balls.focus_set()
    input_balls.bind("<Return>",init_balls)
    time_text = Label(frame_text, text = 'Оставшееся время (сек)', width=20, font='Calibri 14')
    time_Go = Label(frame_text,text = time_limit, font='Calibri 14')
    time_text.grid(row=2, column=0)
    time_Go.grid(row=2, column=1)
    points = 0 # число удаленных шариков
    frame_canvas = Frame(root)
    frame_canvas.pack()
    canvas = Canvas(frame_canvas, background="white", width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()

if __name__ == '__main__':
    init_main_window()
    root.mainloop()
