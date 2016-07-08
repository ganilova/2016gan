from drawman import*
from time import*
A=[(0, 0), (100,0), (100, 100), (0, 100), (0, 0)]
pen_down()
for x, y in A:
    to_point(x, y)
pen_up()
sleep(5)