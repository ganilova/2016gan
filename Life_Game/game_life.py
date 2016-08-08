__author__ = "Tatyana Ganilova"

from tkinter import messagebox
from tkinter.filedialog import *

sleep_time = 50   # задержка между кадрами в милисекундах
cell_size = 20 #размер клетки по умолчанию
field_size = 600     # ширина (высота) игрового поля
pause = True    # истинно, если не запущена игра

class Cell:
    def __init__(self):
        self.size = cell_size

    def set(self,x,y,key):# рисование клетки
        colors = {0:"white", 1:"green"}
        self.avatar = canvas.create_rectangle(x*self.size, y*self.size,
                                (x+1)*self.size, (y+1)*self.size,
                                fill = colors[key], outline = "lightgray")

def mouse_left(event):# изменение статуса ячейки по щелчку ЛКМ
    global cell
    if 0<event.x < field_size and 0<event.y < field_size:# ограничиваем действие мышки полем игры
        x = event.x//cell_size
        y = event.y//cell_size
        if map[x+1][y+1]==0:
            cell.set(x,y,1)
            map[x+1][y+1] = 1
        else:
            cell.set(x,y,0)
            map[x+1][y+1] = 0

def change_map():
    """
    Изменение состояния поля по правилам игры
    проверяются крайние клетки поля
    выполнен переход на противоположный край
    """
    global map
    temp = [[0] * (cell_count+2) for i in range(cell_count+2)]# Массив для хранения нового состояния
    count = 0 #число живых клеток
    for x in range(1,cell_count+1):
            for y in range(1,cell_count+1):
                count+= map[x][y]
                count_life = 0 # число живых клеток в окружении
                for i in range(-1,2):
                    for j in range(-1,2):
                        count_life+=map[x+i][y+j]
                count_life-=map[x][y]
                if map[x][y]==0 and count_life == 3 or map[x][y]==1 and (count_life == 3 or count_life == 2):
                    temp[x][y] = 1
    for x in range(1,cell_count+1):# копируются крайние столбцы (строки)на противоположную сторону
            temp[0][x]=temp[cell_count][x]
            temp[cell_count+1][x]=temp[1][x]
            temp[x][0]=temp[x][cell_count]
            temp[x][cell_count+1]=temp[x][1]
    if map == temp:
        count = 0
    else:
        map = temp
        canvas.delete("all")
        for x in range(1,cell_count+1):
                for y in range(1,cell_count+1):
                    if map[x][y]==1:
                        cell.set(x-1,y-1,1)
                    else:
                        cell.set(x-1,y-1,0)
    return count

def time_event():
    # перевычислить состояние поля с клетками
    if not pause:
        if change_map()==0:
            messagebox.showinfo("Сообщение",'Игра закончена')
            game()
    canvas.after(sleep_time, time_event)

def game():
    global pause
    if pause:
        go_game["text"]='Стоп'
    else:
        go_game["text"]='Старт'
    pause = not pause

def save_file():#сохранение игрового поля в файл
    if pause:
        name_file = asksaveasfilename()+'.txt'
        f = open(name_file,"w")
        f.write(str(cell_size)+'\n') #размер клетки
        for x in range(1,cell_count+1):
            for y in range(1,cell_count+1):
                f.write(str(map[x][y])+'\n')
        f.close()
        messagebox.showinfo("Сообщение",'Файл  успешно сохранён.')
    else:
        messagebox.showinfo("Ошибка",'Операция сохранения файла недоступна во время работы!\n '
                                     'Нажмите Стоп и повторите операцию.')

def load_file():# Чтение игрового поля из файла в массив и вывод поля игры
    global scale, map
    if pause:
        try:
            name_file = askopenfilename(defaultextension='.txt',filetypes=[('Text files','*.txt')])
            f = open(name_file,"r")
            scale.set(int(f.readline().strip())) #считываем размер клетки
            new_field()
            for x in range(1,cell_count+1):
                for y in range(1,cell_count+1):
                    map[x][y] = int(f.readline().strip())
                    if map[x][y]==1:
                        cell.set(x-1,y-1,1)
                    else:
                        cell.set(x-1,y-1,0)
            f.close()
            for x in range(1,cell_count+1):
                map[0][x]=map[cell_count][x]
                map[cell_count+1][x]=map[1][x]
                map[x][0]=map[x][cell_count]
                map[x][cell_count+1]=map[x][1]
        except IOError:
            messagebox.showinfo("Ошибка",'Не могу открыть файл '+name_file)
    else:
        messagebox.showinfo("Ошибка",'Операция открытия файла недоступна во время работы!\n '
                                     'Нажмите Стоп и повторите операцию.')

def close_win():# уничтожаем главное окно со всеми объектами
    root.destroy()

def rules():
    # вывод правил игры
    rule = '  Каждая клетка  может находиться в двух состояниях:'
    rule +=" быть «живой» (зеленая) или быть «мёртвой» (пустой). Распределение " \
           'живых клеток в начале игры называется первым поколением.\n \n' \
           'Каждое следующее поколение рассчитывается на основе предыдущего по таким правилам:\n '
    rule +='      в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;\n '
    rule +='      если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; \n'
    rule +='      если соседей меньше двух или больше трёх, клетка умирает ' \
           '(«от одиночества» или «от перенаселённости»)\n \n '
    rule +='  Игра прекращается, если на поле не останется ни одной «живой» клетки, или если при очередном шаге ни одна из '
    rule +='клеток не меняет своего состояния (складывается стабильная конфигурация).\n \n'
    rule +='  Игрок не принимает прямого участия в игре, а лишь расставляет на поле' \
           'живые клетки левой клавишей "мышки" или загружает начальную конфигурацию из файла'
    rule +=' клеток, которые затем взаимодействуют согласно правилам уже без его участия.\n \n'
    rule +='Созданную конфигурацию первого поколения можно сохранить в файле.'
    messagebox.showinfo("Правила игры",rule )

def init_menu():# создание меню
    m = Menu(root)
    root.config(menu = m)
    fm = Menu(m)
    m.add_cascade(label="Меню", menu=fm)
    fm.add_command(label="Загрузить поле",command=load_file)
    fm.add_command(label="Сохранить поле",command=save_file)
    fm.add_command(label="Правила игры", command=rules)
    fm.add_command(label="Выход", command=close_win)

def new_field(): #Перечерчивание поля с новым размером ячейки
    canvas.delete("all")
    init_field()

def init_field(): # рассчитываем и выводим пустое поле игры
    global cell, canvas, cell_size, cell_count, map,avatars
    cell_size = scale.get()
    cell_count = field_size // cell_size
    map = [[0] * (cell_count+2) for i in range(cell_count+2)]
    cell = Cell()
    for x in range(cell_count):
            for y in range(cell_count):
                cell.set(x,y,0)

def init_main_window():
    global root, canvas, scale, go_game
    root = Tk()
    root.title('Игра "Жизнь"')
    root.minsize(field_size + 140, field_size)
    root.maxsize(field_size + 140, field_size)
    canvas = Canvas(root, width=field_size, height=field_size)
    canvas.pack(side=LEFT)
    canvas.bind('<Button-1>', mouse_left)
    scale_text = Label(root, text='Размер ячейки', font='Calibri 12')
    tab = field_size+25
    len = 10
    scale_text.place(x = tab-5,y = 10)
    scale = Scale(root, from_=5, to=50, orient=HORIZONTAL,resolution=5, length=95)
    scale.place(x = tab,y = 30)
    scale.set(cell_size)
    amend_map = Button(root, text=' Изменить \n поле ',width = len+2, font='Calibri 10', command=new_field)
    amend_map.place(x = tab,y = 80)
    go_game = Button(root, text='Старт', width = len, font='Calibri 12', command=game)
    go_game.place(x = tab,y = 240)
    init_field()
    init_menu()

if __name__ == "__main__":
    """
    Основная программа
    """
    init_main_window()
    time_event()
    root.mainloop()