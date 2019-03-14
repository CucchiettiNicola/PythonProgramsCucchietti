import turtle as t
import random as r
grande = 400
n_turtles = 5
t.setup(grande, grande)
divisioniCampo = grande/(n_turtles+1)
l = []
cont = (0-(grande/2))
uscita = True
t.speed(1)
for i in range(0, n_turtles-1):
    l.append(t.Turtle())
    l[i].penup()
    l[i].setx(0-(grande/2))
    l[i].sety(cont + divisioniCampo)
    l[i].color("red")
    cont = cont + divisioniCampo
l.append(t)
t.penup()
t.setx(0-(grande/2))
t.sety(cont+divisioniCampo)
cont = cont + divisioniCampo
while uscita:
    for i in range(0, n_turtles):
        l[i].forward(r.randrange(0,11))
        if l[i].xcor() > (grande/2):
            uscita = False
            print("turtle ")
            print(i+1)
            print("ha vinto!")
t.done