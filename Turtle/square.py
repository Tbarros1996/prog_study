# Desenhando um Quadrado
import turtle
pen = turtle.Turtle()
def quadrado():
    for i in range(100):
        pen.forward(10)
        pen.right(20)
        pen.forward(10)
quadrado()