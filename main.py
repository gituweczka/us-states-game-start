import pandas
import turtle
from state_on_a_map import StateOnAMap

screen = turtle.Screen()
screen.title("US states quiz game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_on_map = StateOnAMap()
screen.tracer(0)

num_of_guessed_states = 0
states_data = pandas.read_csv("50_states.csv")


def guess_state():
    global num_of_guessed_states
    answer_state = screen.textinput(title=f"{num_of_guessed_states}/50 States Guessed", prompt="What's another state?")

    if answer_state in states_data.values:
        chosen_state = states_data[states_data.state == answer_state]
        state_x = int(chosen_state.x)
        state_y = int(chosen_state.y)

        state_on_map.write_state_name(answer_state, state_x, state_y)
        num_of_guessed_states += 1
    else:
        pass


while num_of_guessed_states < 50:
    guess_state()

if num_of_guessed_states == 50:
    state_on_map.end_quiz()

screen.mainloop()