from tkinter import *
from tkinter import messagebox

frame_sleep_time = 1   # задержка между кадрами в милисекундах
cell_size = 20 #размер клетки по умолчанию
field_size = 600     # ширина (высота) игрового поля
file_name = "map"

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

def mouse_left(event):
    global cell
    if 0<event.x < field_size and 0<event.y < field_size:
        obj = canvas.find_closest(event.x, event.y)#определяет ближайший объект
        print(obj['fill'])
        """if int(obj[key])==0:
            x = event.x//cell_size
            y = event.y//cell_size
            cell.set(x,y,1)"""

"""

class Field:
    def __init__(self, field_file, canvas):

        self._canvas = canvas
        with open(field_file) as file:
            self.matrix = [None] * cells_vertical_number
            self.avatars = [None] * cells_vertical_number
            for yi in range(cells_vertical_number):
                self.matrix[yi] = [None] * cells_horizontal_number
                self.avatars[yi] = [None] * cells_horizontal_number
                line = file.readline().rstrip()
                line += ' '*(cells_horizontal_number - len(line))
                for xi in range(cells_horizontal_number):
                    # любой символ, кроме пробела -- значикт соотв. клетка жива
                    is_cell_alive = 0 if line[xi] == ' ' else 1
                    self.matrix[yi][xi] = is_cell_alive
                    self.avatars[yi][xi] = canvas.create_rectangle(screen_x(xi), screen_y(yi),
                                                                   screen_x(xi+1), screen_y(yi+1),
                                                                   fill=cell_color(is_cell_alive),
                                                                   outline=cell_outline_color(is_cell_alive))

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


def close_win():# уничтожаем главное окно со всеми объектами
    root.destroy()

def rules():
    # вывод правил игры
    rule = 'Каждая клетка  может находиться в двух состояниях:'
    rule +=" быть «живой» или быть «мёртвой» (пустой) \n "
    rule +='Распределение живых клеток в начале игры называется первым поколением.\n' \
           ' Каждое следующее поколение рассчитывается на основе предыдущего по таким правилам:\n '
    rule +='      в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;\n '
    rule +='      если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; \n'
    rule +='      в противном случае (если соседей меньше двух или больше трёх) клетка умирает ' \
           '(«от одиночества» или «от перенаселённости»)\n '
    rule +='Игра прекращается, если на поле не останется ни одной «живой» клетки, если при очередном шаге ни одна из '
    rule +='клеток не меняет своего состояния (складывается стабильная конфигурация) или если конфигурация на очередном '
    rule +='шаге в точности (без сдвигов и поворотов) '
    rule +='повторит себя же на одном из более ранних шагов (складывается периодическая конфигурация).\n \n'
    rule +='Игрок не принимает прямого участия в игре, а лишь расставляет или генерирует начальную конфигурацию «живых»'
    rule +=' клеток, которые затем взаимодействуют согласно правилам уже без его участия (он является наблюдателем).'
    messagebox.showinfo("Правила игры",rule )

def init_menu():# создание меню
    m = Menu(root)
    root.config(menu = m)
    fm = Menu(m)
    m.add_cascade(label="Меню", menu=fm)
    fm.add_command(label="Правила игры", command=rules)
    fm.add_command(label="Выход", command=close_win)

def new_field(): #Перечерчивание поле для игры с новым размером ячейки
    canvas.delete("all")
    init_field()

def init_field(): # рассчитываем и выводим пустое поле игры
    global cell, canvas, cell_size
    cell_size = scale.get()
    cell_count = field_size // cell_size
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
    button_new_field = Button(root, text=' Изменить \n поле ',width = len+2, font='Calibri 10', command=new_field)
    button_new_field.place(x = tab,y = 80)
    start_or_stop = Button(root, text='Старт', width = len, font='Calibri 12')#, command=start_or_stop, font='arial 14')
    start_or_stop.place(x = tab,y = 240)
    save_map = Button(root, text='Сохранить', width = len, font='Calibri 12')#, command=save_to_file)
    save_map.place(x = tab,y = 150)
    button_load = Button(root, text='Открыть', width = len, font='Calibri 12')#, command=load_of_file)
    button_load.place(x = tab,y = 180)
    filename = StringVar()
    filename.set(file_name)
    entry = Entry(root, textvariable = filename, width = len+1, font='Calibri 12')
    entry.place(x = tab,y = 180)
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