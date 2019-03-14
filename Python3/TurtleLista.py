import turtle as t

spostamento = 1
moltiplicatore = 100

lista = ["f", "f", "r", "f", "f", "r", "f", "f", "r", "f", "f", "r", "f", "r", "f", "f", "r", "f", "r", "f", "r", "f", "f"]

t.speed(0)
t.color("green", "red")

for k in lista:
    print(k);
    if k == "f":
        t.forward(spostamento * moltiplicatore)
    if k == "r":
        t.right(90)
    if k == "b":
        t.right(180)
        t.t.forward(spostamento*moltiplicatore)
        t.right(180)
    if k == "l":
        t.left(90)

t.done()