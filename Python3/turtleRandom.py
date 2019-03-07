import turtle as t
import random as r

spostamento = 1
moltiplicatore = 10

t.speed(0)

while True:
    if((r.random()*10)<5):
        t.left(90)
        t.color("red")
    else:
        t.right(90)
        t.color("green")

    t.forward(spostamento*moltiplicatore)

t.done()