import turtle
import os

ws = turtle.Screen()
ws.title("Turtle race by @silk")
ws.setup(width=800,height=600)
ws.bgcolor("black")
ws.tracer(0) # animation drawing off

#class for the objects
class game_obj:
  def obj_type_one(self,obj,shape,color,wid,lenth,yc,xc):
    obj.speed(0)
    obj.shape(shape)
    obj.color(color)
    obj.shapesize(stretch_wid=wid,stretch_len=lenth)
    obj.penup()
    obj.goto(yc,xc)
      
obj = game_obj()

#vertical line left
track_line_vone = turtle.Turtle()
obj.obj_type_one(track_line_vone,"square","red",16,0.1,-300, 0)

#vertical line right
track_line_vtwo = turtle.Turtle()
obj.obj_type_one(track_line_vtwo,"square","red",16,0.1,280,0)

#start line
track_line_start = turtle.Turtle()
obj.obj_type_one(track_line_start,"square","green",7,0.1,-300,-230)

#Horizontal line upper side
track_line_hone = turtle.Turtle()
obj.obj_type_one(track_line_hone,"square","red",0.1,29,-10,160)

#Horizontal line lower side
track_line_htwo = turtle.Turtle()
obj.obj_type_one(track_line_htwo,"square","red",0.1,29,-10,-160)

#Finish line
track_line_finish = turtle.Turtle()
obj.obj_type_one(track_line_finish,"square","yellow",0.1,5,-350,-160)

#turtle blue
racer_one = turtle.Turtle()
obj.obj_type_one(racer_one,"turtle","blue",3,1,-350,-200)

#turtle white
racer_two = turtle.Turtle()
obj.obj_type_one(racer_two,"turtle","white",3,1,-350,-260)

#start
start= turtle.Turtle()
obj.obj_type_one(start,"square","white",1,1,0,-150)
start.hideturtle()
start.write(f"*** Click space Bar to start Game ***", align="center", font=("courier", 24, "normal"))


#result
result = turtle.Turtle()
obj.obj_type_one(result,"circle","white",1,1,0,0)
result.hideturtle()

# Game control direction:
class game_dir():
  def forward(self,obj):
    x = obj.xcor()
    if x < 350:
      x += 10
      obj.setx(x)
      obj.setheading(0)

  def upward(self,obj):
    y = obj.ycor()
    if y < 250:
      y += 10
      obj.sety(y)
      obj.setheading(90)
      
  def backward(self,obj):
    x = obj.xcor()
    if x > -350:
      x -= 10
      obj.setx(x)
      obj.setheading(180)

  def downward(self,obj):
    y = obj.ycor()
    if y > -250:
      y -= 10
      obj.sety(y)
      obj.setheading(270)

#Race border range for the racers
def border(racer):
  yco = racer.ycor()
  xco = racer.xcor()
  if -180 < yco < 180 and -300 < xco < 280:
    racer.goto(-350, -200)
    os.system("afplay bounce.wav&")
      
  if -180 < yco < -160 and -390 < xco < -300:
    racer.goto(-350, -200)
    os.system("afplay bounce.wav&")
      
    

game_running = True
#Main game loop 
def game():
  global game_running, who
  if game_running:
    ws.update()
    
    dir = game_dir()
    ws.listen()
    
    #control buttons:
    #Racer one
    ws.onkeypress(lambda: dir.forward(racer_one),"d")
    ws.onkeypress(lambda: dir.upward(racer_one),"w")
    ws.onkeypress(lambda: dir.backward(racer_one),"a")
    ws.onkeypress(lambda: dir.downward(racer_one),"s")

    #Racer two
    ws.onkeypress(lambda: dir.forward(racer_two),"Right")
    ws.onkeypress(lambda: dir.upward(racer_two),"Up")
    ws.onkeypress(lambda: dir.backward(racer_two),"Left")
    ws.onkeypress(lambda: dir.downward(racer_two),"Down")

    # Border function check
    border(racer_one)
    border(racer_two)
    
    # winner check
    yco1 = racer_one.ycor()
    xco1 = racer_one.xcor()
    yco2 = racer_two.ycor()
    xco2 = racer_two.xcor()
    if -160 < yco1 < -130 and -390 < xco1 < -300:
       who = "Blue"
       racer_two.goto(-350, -200)
       game_running = False
    if -160 < yco2 < -130 and -390 < xco2 < -300:
       who = "White"
       racer_one.goto(-350, -200)
       game_running = False
  #Re_play game 
  if game_running == False:
    result.write(f"       ***** Game Over *****   \n****  {who} Player is the winner **** \n   *** Do you want to play again *** \n      ** Then press space bar **", align="center", font=("courier", 24, "normal"))
    ws.listen()
    ws.onkeypress(play,"space")
  ws.ontimer(game, 16)
     
#Play and replay functiojn
def play():
  global game_running
  game_running = True
  ws.onkeypress(None,"space")
  start.clear()
  result.clear()
  game()

ws.listen()
ws.onkeypress(play,"space")
turtle.done()
