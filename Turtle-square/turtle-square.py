import turtle

def kare(a):
    for i in range(4):
        ok.color(renkler[i%4])
        ok.forward(a)
        ok.left(90)

renkler = ['red', 'blue', 'green', 'yellow']
turtle.bgcolor("black")

ok = turtle.Turtle()
ok.speed(0)

kenar = 10
for i in range(36):
    kare(kenar)
    kenar = kenar + 10
    ok.right(10)