from drawman import*
from time import*
def f(x):
    return x*x

drawman_csale = 20
x=-5.0
pen_down()
to_point(x, f(x))
while x<=5:
    to_point(x, f(x))
    x+=0.1
pen_up()
sleep(5)