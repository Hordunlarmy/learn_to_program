import turtle

# Set up the screen
pong = turtle.Screen()
pong.title("PONG GAME BY ODUN")
pong.bgcolor("black")
pong.setup(width=800, height=600)
pong.tracer(0)

# Score write up
scoreA = 0
scoreB = 0
pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {scoreA}  Player B: {scoreB}",
          align="center", font=("Courier", 24, "bold"))

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25

# Paddle A function


def paddleA_up():
    y = paddleA.ycor()
    if y > 390:
        paddleA.sety(390)
    y += 20
    paddleA.sety(y)


def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

# Paddle B function


def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# key biddings
pong.listen()
pong.onkeypress(paddleA_up, "w")
pong.onkeypress(paddleA_down, "s")
pong.onkeypress(paddleB_up, "Up")
pong.onkeypress(paddleB_down, "Down")

# Main game loop
try:
    while True:
        pong.update()

        # ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # boarder control
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            scoreA += 1
            pen.clear()
            pen.write(f"Player A: {scoreA}  Player B: {scoreB}",
                      align="center", font=("Courier", 24, "bold"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            scoreB += 1
            pen.clear()
            pen.write(f"Player A: {scoreA}  Player B: {scoreB}",
                      align="center", font=("Courier", 24, "bold"))

        # ball and paddle colission
        if (ball.xcor() < -340 and ball.xcor() > -350 and
            ball.ycor() < paddleA.ycor() + 40 and
                ball.ycor() > paddleA.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1

        if (ball.xcor() > 340 and ball.xcor() < 350 and
                ball.ycor() < paddleB.ycor() + 40 and
                ball.ycor() > paddleB.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
except:
    print("Game Successfully Exited")
