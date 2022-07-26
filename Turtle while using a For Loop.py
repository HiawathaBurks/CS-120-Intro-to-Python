import turtle as tu

tpen = tu.Pen()
tpen.speed(0)

for x in range(360):
    tpen.pencolor("white")
    tpen.width(1)
    tpen.forward(x)
    tpen.left(59)
    tpen.penup()
    tpen.forward(x)
    tpen.left(59)
    tpen.pendown()

tpen.penup()
tpen.home()
tpen.pendown()

for x in range(360):
    tpen.pencolor("white")
    tpen.width(1)
    tpen.backward(x)
    tpen.right(-59)
    tpen.penup()
    tpen.backward(x)
    tpen.right(-59)
    tpen.pendown()


Cppsecrets = tu.Screen()
Cppsecrets.bgcolor('black')
s = tu.Turtle()
s.speed('fastest')
s.color('white')
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
t1.color('yellow')
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

roo = tu.Turtle()  # Turtle object
wn = tu.Screen()  # Screen Object
wn.bgcolor("black")  # Screen Bg color
wn.title("Fractal Tree Pattern")
roo.left(90)  # moving the turtle 90 degrees towards left
roo.speed(20)  # setting the speed of the turtle


def draw(l):  # recursive function taking length 'l' as argument
    if (l < 10):
        return
    else:

        roo.pensize(2)  # Setting Pensize
        roo.pencolor("yellow")  # Setting Pencolor as yellow
        roo.forward(l)  # moving turtle forward by 'l'
        roo.left(30)  # moving the turtle 30 degrees towards left
        draw(3 * l / 4)  # drawing a fractal on the left of the turtle object 'roo' with 3/4th of its length
        roo.right(60)  # moving the turtle 60 degrees towards right
        draw(3 * l / 4)  # drawing a fractal on the right of the turtle object 'roo' with 3/4th of its length
        roo.left(30)  # moving the turtle 30 degrees towards left
        roo.pensize(2)
        roo.backward(l)  # returning the turtle back to its original psition


draw(20)  # drawing 20 times

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")  # magenta
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

roo.left(270)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("red")  # red
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC')  # white
        roo.forward(l)
        roo.left(30)
        draw(3 * l / 4)
        roo.right(60)
        draw(3 * l / 4)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(20)


########################################################

def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(3)
        roo.pencolor("lightgreen")  # lightgreen
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("red")  # red
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.left(270)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor("yellow")  # yellow
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(3)
        roo.pencolor('#FFF8DC')  # white
        roo.forward(l)
        roo.left(30)
        draw(4 * l / 5)
        roo.right(60)
        draw(4 * l / 5)
        roo.left(30)
        roo.pensize(3)
        roo.backward(l)


draw(40)


########################################################
def draw(l):
    if (l < 10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("cyan")  # cyan
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")  # yellow
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)

roo.left(270)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor("magenta")  # magenta
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)

roo.right(90)
roo.speed(2000)


# recursion
def draw(l):
    if (l < 10):
        return
    else:
        roo.pensize(2)
        roo.pencolor('#FFF8DC')  # white
        roo.forward(l)
        roo.left(30)
        draw(6 * l / 7)
        roo.right(60)
        draw(6 * l / 7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)


draw(60)
wn.exitonclick()
