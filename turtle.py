import turtle


screen = turtle.Screen()
t = turtle.Turtle()
t.speed(30)

turtle.bgcolor('black')
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

colors = ["blue", "white", "white", "white","white","red","red","red","white","red","red","red","white","red","red","red"]
cnt = 0

for i in range(4):
    for j in range(4):
        draw_rectangle(j * 100, i * 100, 100, 100, colors[cnt])
        print(j*100,i*100)
        cnt += 1

t.penup()
t.pensize(5)
t.color("black")
t.goto(0,0)
t.pendown()
t.goto(100,0)
t.goto(100,-100)
t.goto(-100,-100)
t.goto(400,-100)
t.goto(400,0)
t.goto(100,0)
print("위에 줄 출격")
t.goto(100,400)
t.goto(0,400)
print("색칠 완료")
t.penup()
t.goto(400,-100)
t.pendown()
t.color("yellow")
t.pensize(1)
t.begin_fill()
t.goto(350,-100)
t.goto(350,-50)
t.goto(400,-50)
t.end_fill()

t.penup()
t.pensize(5)
t.color("black")
t.goto(350,0)
t.pendown()
t.goto(350,-100)
t.goto(400,-100)
t.goto(400,0)
t.goto(400,-50)
t.goto(350,-50)

t.penup()
t.pensize(6)
t.goto(100,150)
t.pendown()
t.goto(0,150)
screen.mainloop()
