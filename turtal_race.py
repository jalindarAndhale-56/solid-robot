from itertools import count
from  turtle import  Turtle,Screen
import  random
height,width=400,400
color_list=["red","green","pink","yellow","black","blue","orange","brown","purple",
            "navy","sky blue","indigo","rose","ruby","amber","umber","chestnut"]

def on_of_turtle():
    count=0
    while True:
        count=input(" enter how many turtles you want ot participate 1-10: ")
        if count.isdigit():
            count=int(count)
        else:
            print(" please enter a numeric value between 2 t0 10...")
            continue
        if 2<= count <=10:
            return  count
        else:
            print(" input is not in given range...")

turtles=on_of_turtle()
print(turtles)

s1=Screen()
s1.setup(400,400)

x_space=width//(turtles+1)
turtle_list=[]
for i in range(1,turtles+1):
    new_tom=Turtle()
    new_tom.shape("turtle")
    new_tom.left(90)
    new_tom.color(color_list[i-1])
    new_tom.penup()
    new_tom.goto(-width//2 + (i*x_space), -height//2 + 10)
    turtle_list.append(new_tom)


def race():
    is_race_on=True
    while is_race_on:
        for turtle in turtle_list:
            distance=random.randrange(1,20)
            turtle.forward(distance)

            x,y=turtle.pos()

            if y>= height//2-20:
                print(f" winner is{turtle.color()} turtle ")
                is_race_on=False
race()
s1.exitonclick()