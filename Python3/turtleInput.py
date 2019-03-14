import turtle as t

spostamento = 1
moltiplicatore = 100

t.speed(0)
t.color("green", "red")

while True:
    k = input()
    if k == "f":
        t.forward(spostamento * moltiplicatore)
    if k == "r":
        t.right(90)
    if k == "b":
        t.right(180)
        t.forward(spostamento*moltiplicatore)
        t.right(180)
    if k == "l":
        t.left(90)
    if k == "stop":
        break

t.done()