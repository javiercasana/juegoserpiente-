"""
Créditos de donde he sacado el juego
https://www.youtube.com/watch?v=lKzEvbGbbPo&list=LL&index=1

"""

import turtle 
import time 
import random

delay = 0.1
body_segments = []
score = 0
high_score = 0


wn = turtle.Screen()


wn.title("Juego Snake")

wn.setup(width= 600, height= 600)

wn.bgcolor("light green")

#head snake

head = turtle.Turtle()
#velocidad cabeza
head.speed(0)
#forma cabeza
head.shape("square")
#color cabeza
head.color("green")
#centrar cabeza
head.goto(0, 0)
#direccion inicial
head.direction = "stop"
#para que no deje estala 
head.penup()





#Food config
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.direction = "stop"


#MARCADOR
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
#Tipo de letra del score
text.write(f"Score 0        High Score: 0",align="center",font=("Impact",24))
           
          






def group():
    if head.direction != "down":
        head.direction = "up"
 
 
def godown():
    if head.direction != "up":
        head.direction = "down"
 
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
 
def goright():
    if head.direction != "left":
        head.direction = "right"
 
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
 
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
while True :#Y aqui le decimos que mientras funcione se actualice y funcionen los ejes 
    wn.update()


#Colisiones con la comida
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
#Esconder segmentos
        for segment in body_segments:
            segment.goto(1000, 1000)
#Con esto limpiamos los segmentos cuadno acaba el juego
        body_segments.clear()
        score = 0
        text.clear()
        text.write(f"score {score}        High Score: {high_score}",align="center",font=("Impact",24))





#Colisiones con la comida
    if head.distance(food) < 20 :
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)





#New segment body   
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        body_segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        text.clear()
        text.write(f"score {score}        High Score: {high_score}",align="center",font=("Impact",24))

    
    totalSeg = len(body_segments)   


#Esto es para que los segmentos del cuerpo se añadan uno detrás del otro
    for i in range(totalSeg -1, 0 , -1):
        x = body_segments[i -1].xcor()
        y = body_segments[i -1].ycor()
        body_segments[i].goto(x,y)
#Esto es para que seañadan detrás de la cabeza dichos segmentos 
    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)
        
    move()
#colisiones con los segmentos del cuerpo
    for segment in body_segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #esconder los segmentos de nuevo
            for segment in body_segments:
                segment.goto(1000, 1000)
            #borrar los segmentos de nuevo
            body_segments.clear()
            score = 0
            text.clear()
            text.write(f"score {score}        High Score: {high_score}",align="center",font=("Impact",24))
            


    time.sleep(delay)

turtle.done()