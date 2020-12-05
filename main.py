import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("yellow")
turtle.setup(600, 600)
turtle.shape("turtle")

screen = turtle.Screen()

Jane = turtle.Turtle()

def EqiTriangle(length, color):
  Jane.fillcolor(color)
  Jane.begin_fill()

  x=0
  while x<3:
    Jane.forward(int(length))
    Jane.right(120)
    x=x+1
  Jane.end_fill()

def Circle(length, color):
  Jane.fillcolor(color)
  Jane.begin_fill()

  x=0
  while x<100:
    Jane.forward(int(length))
    Jane.right(3.6)
    x=x+1
  Jane.end_fill()

def Star(length, color):
  Jane.fillcolor(color)
  Jane.begin_fill()

  x=0
  while x<5:
    Jane.forward(int(length))
    Jane.right(150)
    x=x+1
  Jane.end_fill()

input_shape = input("What shape would you lie to draw?:  ")
length_shape = input("What length would you like your shape to have?: ")
color_shape = input("What color would you like your shape to be?  ")

if input_shape == 'triangle':
  EqiTriangle(length_shape, color_shape)
elif input_shape == 'circle':
  Circle(length_shape, color_shape)
elif input_shape == 'star':
  Star(length_shape, color_shape)

turtle.done()