import turtle
bob = turtle.Turtle()
n = 20
length = 30

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob, 7, 70)