from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import fileinput

frame_sleep_time = 1   # задержка между кадрами в милисекундах
cell_size = 20 #размер клетки по умолчанию
field_size = 600     # ширина (высота) игрового поля
file_name = "map"
pause = True

class Cell:
    def __init__(self):
        self.size = cell_size
        self.key = 0

    def set(self,x,y,key):# рисование клетки
        colors = {0:"white", 1:"green"}
        self.x = x
        self.y = y
        self.key = key
        self.avatar = canvas.create_rectangle(y*self.size, x*self.size,
                                (y+1)*self.size, (x+1)*self.size,
                                fill = colors[self.key], outline = "lightgray")

    def delete(self):
        canvas.delete(self.avatar)

def mouse_left(event):# изменение поля игры
    global cell
    if 0<event.x < field_size and 0<event.y < field_size:
        x = event.x//cell_size
        y = event.y//cell_size
        if matrix[y][x]==0:
            cell.set(y,x,1)
            matrix[y][x] = 1
        else:
            cell.set(y,x,0)
            matrix[y][x] = 0

"""
    def calculate(self):
        """  """
        # рассчитываем матрицу состояний клеток на следующем шаге
        new_matrix = [[0]*cells_horizontal_number for i in range(cells_vertical_number)]
        for yi in range(1, cells_vertical_number-1):
            for xi in range(1, cells_horizontal_number-1):
                # подсчитаем количество живых соседей
                number_of_neighbours = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        number_of_neighbours += self.matrix[yi+i][xi+j]
                number_of_neighbours -= self.matrix[yi][xi]
                cell_is_alive = self.matrix[yi][xi]
                if (cell_is_alive and number_of_neighbours == 2) or number_of_neighbours == 3:
                    new_matrix[yi][xi] = 1
                else:
                    new_matrix[yi][xi] = 0
        # копируем рассчитанную матрицу в self.matrix
        for yi in range(1, cells_vertical_number-1):
            for xi in range(1, cells_horizontal_number-1):
                if self.matrix[yi][xi] != new_matrix[yi][xi]:
                    self.matrix[yi][xi] = new_matrix[yi][xi]
                    self._canvas.delete(self.avatars[yi][xi])
                    self.avatars[yi][xi] = self._canvas.create_rectangle(screen_x(xi), screen_y(yi),
                                                                         screen_x(xi+1), screen_y(yi+1),
                                                                         fill=cell_color(new_matrix[yi][xi]),
                                                                         outline=cell_outline_color(new_matrix[yi][xi]))

def time_event():
    global scores
    # перевычислить состояние поля с клетками
    field.calculate()
    canvas.after(frame_sleep_time, time_event)
"""
def save_file():#сохранение игрового поля в файл
    if pause:
        name_file = asksaveasfilename()+'.txt'
        f = open(name_file,"w")
        f.write(str(cell_size)+'\n') #размер клетки
        for y in range(0,cell_count):
            for x in range(0,cell_count):
                f.write(str(matrix[x][y])+'\n')
        f.close()
        messagebox.showinfo("Сообщение",'Файл  успешно сохранён.')
    else:
        messagebox.showinfo("Ошибка",'Операция сохранения файла недоступна во время работы!')

def load_file():# Чтение игрового поля из файла в массив
    global scale, matrix
    if pause:
        try:
            name_file = askopenfilename(defaultextension='.txt',filetypes=[('Text files','*.txt')])
            f = open(name_file,"r")
            scale.set(int(f.readline().strip())) #размер клетки
            new_field()
            for y in range(0,cell_count):
                for x in range(0,cell_count):
                    matrix[x][y] = int(f.readline().strip())
                    if matrix[x][y]==1:
                        cell.set(x,y,1)
                    else:
                        cell.set(x,y,0)
            f.close()
        except IOError:
            messagebox.showinfo("Ошибка",'Не могу открыть файл '+name_file)
    else:
        messagebox.showinfo("Ошибка",'Операция открытия файла недоступна во время работы!')

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
    rule +='  Игрок не принимает прямого участия в игре, а лишь расставляет или загружает из файла начальную конфигурацию «живых»'
    rule +=' клеток, которые затем взаимодействуют согласно правилам уже без его участия.'
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

def new_field(): #Перечерчивание поле для игры с новым размером ячейки
    canvas.delete("all")
    init_field()

def init_field(): # рассчитываем и выводим пустое поле игры
    global cell, canvas, cell_size, cell_count, matrix
    cell_size = scale.get()
    cell_count = field_size // cell_size
    matrix = [[0] * cell_count for i in range(cell_count)]
    cell = Cell()
    for x in range(cell_count):
            for y in range(cell_count):
                cell.set(x,y,0)

def init_main_window():
    global root, canvas, scale
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
    start_or_stop = Button(root, text='Старт', width = len, font='Calibri 12')#, command=start_or_stop, font='arial 14')
    start_or_stop.place(x = tab,y = 240)
    init_field()
    init_menu()



if __name__ == "__main__":
    """
    Основная программа
    """
    init_main_window()
    root.mainloop()
    """     мусор
    canvas.bind('<Motion>', mouse_move)
    field = Field('map2.txt', canvas)
    time_event()  # начинаю циклически запускать таймер
    """