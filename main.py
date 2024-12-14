from turtle import Turtle, Screen
import random
tim = Turtle(shape='turtle')
tom = Turtle(shape='turtle')
tam = Turtle(shape='turtle')
tem = Turtle(shape='turtle')
tum = Turtle(shape='turtle')
tin = Turtle(shape='turtle')
tig = Turtle(shape='turtle')
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Turtles: violet,purple,blue,green,yellow,orange,red\nWhich turtle will win the race?\nEnter a color: ")
turtle = {tim: 'violet', tom: 'purple', tam: 'blue', tem: 'green', tum: 'yellow', tin: 'orange', tig: 'red'}
y = -80
for i in turtle:
    i.penup()
    choice = turtle[i]
    i.color(choice)
    i.goto(x=-230, y=y)
    y += 25
is_race = False
if user_bet:
    is_race = True
while is_race:
    for i in turtle:
        move = random.randint(0, 10)
        i.forward(move)
        if i.xcor() > 230:
            is_race = False
            win = i.pencolor()
            if user_bet == win:
                print("You won the bet!")
            else:
                print(f"{win} won!")
                print("Better luck next time..")
screen.exitonclick()
