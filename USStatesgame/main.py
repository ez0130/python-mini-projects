import turtle
import pandas as pd

scoreboard = turtle.Turtle()
screen = turtle.Screen()

'''
turtle.listen()
def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
'''

image = "E:/cs50/US states map game/blank_states_img.gif"
screen.bgpic(image)
screen.title("States guessing game")

answer = screen.textinput(title="States", prompt="Guess States").title()

game_is_on = True


df = pd.read_excel("E:/cs50/US states map game/asdf.xlsx")
states = df.state.to_list()

guessed_answer=[]

scoreboard.penup()
scoreboard.hideturtle()
scoreboard.score = 50
def update_scoreboard():
    scoreboard.clear()
    scoreboard.goto(0, 250)
    scoreboard.write(scoreboard.score , align="center", font=("Courier", 80, "normal"))


update_scoreboard()

'''
with open ("E:/cs50/US states map game/50_states.csv", 'r') as f:
    read_lines = f.readline()
    while read_lines:
        state = read_lines.strip().split(',')
        states[state[0]] = {state[1], state[2]}
        read_lines = f.readline()

'''
print(states)
guessed_answer=[]


while game_is_on:
    if answer == "Exit":
        break
    if answer not in guessed_answer and answer in states:
        turtle.penup()
        state_data = df[df.state == answer]
        turtle.goto(int(state_data.x), int(state_data.y))
        turtle.write(answer)
        scoreboard.score -= 1
        update_scoreboard()
        if scoreboard.score == 0:
            turtle.goto(0, -250)
            turtle.pencolor("blue")
            turtle.write("congratulations!", align = "center" , font = ("Courier", 60))
            game_is_on = False
    answer = screen.textinput(title="States", prompt="Guess States").title()


screen.exitonclick()
