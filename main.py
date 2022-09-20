import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state name?").title()

    if answer_state == "Exit":
        unguessed_states = [i for i in states if i not in guessed_states]
        new_data = pandas.DataFrame(unguessed_states)
        new_data.to_csv("States to Learn.csv")
        break

    elif answer_state in states:
        state_cord = data[data.state == answer_state]
        x_cord = state_cord.x
        y_cord = state_cord.y
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x_cord), int(y_cord))
        t.write(answer_state)
        guessed_states.append(answer_state)
    else:
        print("nothing yet")

