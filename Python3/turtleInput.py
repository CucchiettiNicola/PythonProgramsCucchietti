import turtle as t

spostamento = 1
moltiplicatore = 100

t.speed(0)
t.color("green", "red")

while True:
    print("\ninserire:\nf per andare avanti\nr per girare a destra\nl per girare a sinistra\nb per andare indietro\nstop per fermare il programma\n |\n\ /")
    k = input()
    if k == "f":
        t.forward(spostamento * moltiplicatore)
    else:
        if k == "r":
            t.right(90)
        else:
            if k == "b":
                t.right(180)
                t.forward(spostamento*moltiplicatore)
                t.right(180)
            else:
                if k == "l":
                    t.left(90)
                else:
                    if k == "stop":
                        break
                    else:
                        print("\ncomando inserito sbagliato")

t.done()