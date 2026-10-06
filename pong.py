import turtle
import os


wn = turtle.Screen()
wn.title("Pong by @silkEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)



class game_objects:
  def objects_one(self,obj,shape,width,lenght,yc,xc):
    obj.speed(0)
    obj.shape(shape)
    obj.color("white")
    obj.shapesize(stretch_wid=width,stretch_len=lenght)
    obj.penup()
    obj.goto(yc,xc)
  
go = game_objects()
score_a = 0
score_b = 0
#Oject creation:
#  go.objects_one(obejct name,shape of object,shape_size wid,shape_size len, y codinate, x codinate, )

#Paddle left side
paddle_a = turtle.Turtle()
go.objects_one(paddle_a,"square",5,1,-350,0)

#Paddle right side
paddle_b = turtle.Turtle()
go.objects_one(paddle_b,"square",5,1,350,0)

#Ball
ball = turtle.Turtle()
go.objects_one(ball,"circle",1,1,0,0)
# Ball Movement
ball.dx = 4
ball.dy = -4

#Pen
pen = turtle.Turtle()
go.objects_one(pen,"circle",1,1,0,260)
pen.hideturtle()
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("courier", 24, "normal"))

#Result
result = turtle.Turtle()
go.objects_one(result,"circle",1,1,0,-80)
result.hideturtle()

replay = turtle.Turtle()
go.objects_one(replay,"triangle",1,1,0,-150)
replay.hideturtle()
replay.write(f"*** Click space to start Game ***", align="center", font=("courier", 24, "normal"))


class game_direction:
  def paddle_up(self,obj):
    y = obj.ycor()
    if y < 240:
      y += 20
      obj.sety(y)
  
  def paddle_down(self,obj):
    y = obj.ycor()
    if y > -240:
      y -= 20
      obj.sety(y)

    
    

# Keyboard binding:
dir = game_direction()
wn.listen()
wn.onkeypress(lambda: dir.paddle_up(paddle_a),"w")
wn.onkeypress(lambda: dir.paddle_down(paddle_a),"s")
wn.onkeypress(lambda: dir.paddle_up(paddle_b),"Up")
wn.onkeypress(lambda: dir.paddle_down(paddle_b),"Down")

game_running = True
#Main game loop
def game():
  global game_running
  if game_running:
    result.clear()
    replay.clear()
    global score_a, score_b, who
    wn.update()
    pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("courier", 24, "normal"))
    #Ball movement
    ball.setx(ball.xcor() +ball.dx)
    ball.sety(ball.ycor() +ball.dy)
    
    #Border checking
    if ball.ycor() > 290:
      ball.sety(290)
      ball.dy *= -1
      os.system("afplay bounce.wav&")
      
    if ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1
      os.system("afplay bounce.wav&")
      
    if ball.xcor() > 390:
      ball.goto(0,0)
      ball.dx *= -1
      score_a += 1
      pen.clear()
      # show Reseted score 
      pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("courier", 24, "normal"))
      
    if ball.xcor() < -390:
      ball.goto(0,0)
      ball.dx *= -1
      score_b += 1
      pen.clear()
      pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("courier", 24, "normal"))
    
    #Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
      (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() -55):
      ball.setx(340)
      ball.dx *= -1
      os.system("afplay bounce.wav&")
    
    if (ball.xcor() < -340 and ball.xcor() < -350) and \
      (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() -55):
      ball.setx(-340)
      ball.dx *= -1
      os.system("afplay bounce.wav&")
      
    #Check winner
    if score_a == 3:
      replay.write(f"*** Do you want to play again ***\n  *** Then press space bar ***", align="center", font=("courier", 24, "normal"))
      who = "A"
      game_running = False
    if score_b == 3:
      replay.write(f"*** Do you want to play again ***\n  *** Then press space bar ***", align="center", font=("courier", 24, "normal"))
      who = "B"
      game_running = False
    wn.ontimer(game, 16)
  if game_running == False:
    result.write(f"***** Game Over ***** \nPlayer {who} is the winner", align="center", font=("courier", 24, "normal"))
    #it will reset the score
    score_a = 0
    score_b = 0
    wn.listen()
    wn.onkeypress(re_play,"space")
    
#its a replay function and also work like frist game run    
def re_play():
  global game_running
  game_running = True
  wn.onkeypress(None, "space")
  pen.clear()
  game()
  
wn.listen()
wn.onkeypress(re_play,"space")
turtle.done()



