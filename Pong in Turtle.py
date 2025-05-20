import turtle
#window & background
wn = turtle.Screen() # wn = window
wn.title = ("Pong") 
wn.bgcolor("black") # bg = background
wn.setup(width=800, height=600)
wn.tracer(0) # tracer stops the window from updating, so we have to manually update it 

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Animation speed not movement 
paddle_a.shape("square") # 20 px x 20 px default size
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup() # Because we don't want to draw a line when it moves
paddle_a.goto(-350, 0)


# Paddle B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")  
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup() 
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")  
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Ball movement
ball.dx = 2 # d means change
ball.dy = 2 # this two variables mean everytime the ball moves it moves 2 pixels

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # hide it because we don't wanna see, only text is required
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score 
score_a = 0
score_b = 0 



# Function for paddle movement:

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 
    paddle_b.sety(y)
    
# Keyboard binding 
wn.listen() # this tells the computer to listen for keyboard inputs
wn.onkeypress(paddle_a_up, "w") # when user presses w it calls paddle_a_up 
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")    # Up is the up arrow key 
wn.onkeypress(paddle_b_down, "Down")   # Down is the down arrow key 

# Main game loop 
while True:
    wn.update() # what update does is basically it updates the screen everytime the loop runs 
    
    # Move the ball 
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking 
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1 # this should reverse the direction of the ball as it is - 1 
    
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() >390:
        ball.goto(0, 0) # this puts the ball back to the center
        ball.dx *= -1 
        score_a += 1 
        pen.clear() # this wil clear the number before we update the score
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)# this puts the ball back to the center
        ball.dx *= -1
        score_b += 1 
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
    
    # Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 