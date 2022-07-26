import turtle as tu

Cppsecrets = tu.Screen()
Cppsecrets.bgcolor('black')
s = tu.Turtle()
s.speed('fastest')
s.color('pink')
rotate=int(180)
def Circles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def Cppsecrets1(t,size,repeat):
  for i in range (repeat):
    Circles(t,size)
    t.right(360/repeat)
Cppsecrets1(s,200,10)
t1 = tu.Turtle()
t1.speed(0)
t1.color('purple')
rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def Cppsecrets1(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
Cppsecrets1(t1,160,10)
t2= tu.Turtle()
t2.speed(0)
t2.color('blue')
rotate=int(80)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def Cppsecrets1(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
Cppsecrets1(t2,120,10)
"""
t3 = tu.Turtle()
t3.speed(0)
t3.color('red')
rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def Cppsecrets1(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
Cppsecrets1(t3,80,10)
t4= tu.Turtle()
t4.speed(0)
t4.color('green')

rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def Cppsecrets1(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
Cppsecrets1(t4,40,10)
"""
win = tu.Screen() #background color of the window
z = tu.Turtle()
z.speed(0)

#outline of the circle
z.color("white") #Use to set the color of the turtle 
z.right(90)
z.forward(200)
z.left(90)
z.color("black")
z.fillcolor("white")
z.begin_fill()
z.circle(200)
z.end_fill()

#Now creating the smaller black circle
z.color("white")
z.left(90)
z.forward(400)
z.color("black")
z.fillcolor("black")
z.begin_fill()
z.left(90)
z.circle(100)
z.end_fill()

#Now black filling color in bigger semicircle
z.fillcolor("black")
z.begin_fill()
z.left(90)
z.forward(400)
z.left(90)
z.circle(200,180)
z.end_fill()

#Now creating smaller circle
z.left(90)
z.forward(200)
z.color("white")
z.fillcolor("white")
z.begin_fill()
z.right(90)
z.circle(99)
z.end_fill()

#Now creating the white eye
z.color("black")
z.right(90)
z.forward(75)
z.right(90)
z.fillcolor("white")
z.begin_fill()
z.circle(25)
z.end_fill()

#Now creating the black eye
z.right(90)
z.forward(75)
z.color("white")
z.forward(75)
z.right(90)
z.fillcolor("black")
z.begin_fill()
z.circle(25)
z.end_fill()

tu.done()
