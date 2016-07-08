import turtle

def init_drawman():
    global t, x_current, y_current, draw_scale
    default_scale = 0
    while default_scale<10 or default_scale>50:
            print('Введите число от 10 до 50 (масштаб координатной сетки)')
            default_scale=int(input())
    t=turtle.Turtle()
    x_current=0
    y_current=0
    drawman_scale(default_scale)
    turtle.setup(20*default_scale,20*default_scale)#устанавливаем размеры экрана
    grid(default_scale)
    axis(default_scale)
    x_current=0
    y_current=0
    t.goto(x_current,y_current)

def axis(scale): #координатные оси
    # ось Х
    t.penup()
    t.goto(-scale*10, 0)
    t.pendown()
    t.goto(scale*10-10,0)
    # стрелочка на оси Х
    x,y=t.pos()
    t.begin_fill()
    t.goto(x-10,y+10)
    t.goto(x-10,y-10)
    t.goto(x,y)
    t.end_fill()
    #  ось У
    t.penup()
    t.goto(0,-scale*10)
    t.pendown()
    t.goto(0,scale*10-10)
    # стрелочка на оси У
    x,y=t.pos()
    t.begin_fill()
    t.goto(x-10,y-10)
    t.goto(x+10,y-10)
    t.goto(x,y)
    t.end_fill()
    t.penup()
def grid(scale):    # рисуем сетку
    t.color ('lightgray')
    x=-10*scale # вертикальные
    for k in range(20):
        t.penup()
        t.goto(x,-scale*10)
        t.pendown()
        t.goto(x, scale*10)
        x+=scale
    y=10*scale # горизонтальные
    for k in range(20):
        t.penup()
        t.goto(-scale*10, y)
        t.pendown()
        t.goto(scale*10, y)
        y-=scale
    t.color('black')
    t.penup()

def drawman_scale(scale):
    global draw_scale
    draw_scale=scale

def test_drawman():
    pen_down()
    for i in range (5):
        on_vector(10, 20)
        on_vector(0, -20)
    pen_up()
    to_point(0, 0)

def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx, dy):
    to_point(x_current+dx, y_current+dy)

def to_point(x, y):
    global  x_current, y_current
    x_current=x
    y_current=y
    t.goto(draw_scale * x_current,draw_scale * y_current)

init_drawman()
if __name__ == '__main__':
    import time
    #test_drawman()
    time.sleep(15)