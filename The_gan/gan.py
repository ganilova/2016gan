from tkinter import *
from random import choice, randint


screen_width = 400
screen_height = 400
timer_delay = 20
initial_number = 20

class Ball:
    minimal_radius = 15
    maximal_radius = 30
    available_colors = ['green', 'blue', 'red']

    def __init__(self):
        """
        Cоздаёт шарик в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста!
        """
        R = randint(Ball.minimal_radius, Ball.maximal_radius)
        x = randint(0, screen_width-1-2*R)
        y = randint(0, screen_height-1-2*R)
        self._R = R
        self._x = x
        self._y = y
        fillcolor = choice(Ball.available_colors)
        self.avatar = canvas.create_oval(x, y, x+2*R, y+2*R,
                                          width=1, fill=fillcolor,
                                          outline=fillcolor)
        dx = 0
        while dx ==0:
            dx = randint(-2, 2)
        dy = 0
        while dy ==0:
            dy = randint(-2, 2)
        self._Vx = dx
        self._Vy = dy

    def fly(self):
        self._x += self._Vx
        self._y += self._Vy
        # отбивается от горизонтальных стенок
        if self._x < 0:
            self._x = 0
            self._Vx = -self._Vx
        elif self._x + 2*self._R >= screen_width:
            self._x = screen_width - 2*self._R
            self._Vx = -self._Vx
        # отбивается от вертикальных стенок
        if self._y < 0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y + 2*self._R >= screen_height:
            self._y = screen_height - 2*self._R
            self._Vy = -self._Vy

        canvas.coords(self.avatar, self._x, self._y,
                      self._x + 2*self._R, self._y + 2*self._R)
    def delete(self):# удаление экземпляра
        canvas.delete(self.avatar)

class Gun:
    def __init__(self):
        self._x = 0
        self._y = screen_height-1
        self._lx = +30
        self._ly = -30
        self._avatar = canvas.create_line(self._x, self._y,
                                          self._x+self._lx,
                                          self._y+self._ly)

    def shoot(self):
        """
        :return возвращает объект снаряда (класса Ball)
        """
        shell = Ball()
        shell._x = self._x - 5 + self._lx
        shell._y = self._y - 5+ self._ly
        shell._Vx = self._lx/10
        shell._Vy = self._ly/10
        shell._R = 5
        shell.fly()
        return shell


def init_game():
    """
    Создаём необходимое для игры количество объектов-шариков,
    а также объект - пушку.    """
    global balls, gun, shells_on_fly
    balls = [Ball() for i in range(initial_number)]
    gun = Gun()
    shells_on_fly = []

def init_main_window():
    global root, canvas, scores_text, scores_value
    root = Tk()
    root.title("Пушка")
    root.minsize(450, 550)
    root.maxsize(450, 550)
    scores_value = IntVar()
    canvas = Canvas(root, width=screen_width, height=screen_height,
                    bg="white")
    scores_text = Entry(root, textvariable=scores_value)
    canvas.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0, column=2)
    canvas.bind('<Button-1>', click_event_handler)


def timer_event():
    # все периодические рассчёты, которые я хочу, делаю здесь
    for ball in balls:
        ball.fly()
    for shell in shells_on_fly:
        # Проверка вылета снаряда за пределы поля
        if shell._x+shell._Vx>screen_width or shell._y+shell._Vy<0 or  shell._x - shell._Vx<0 or shell._y + shell._Vy>screen_height:
            shell.delete()
        else:
            shell.fly()
    canvas.after(timer_delay, timer_event)

def click_event_handler(event):
    global shells_on_fly
    shell = gun.shoot()
    shells_on_fly.append(shell)

if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()