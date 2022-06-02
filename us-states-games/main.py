import turtle
import pandas

screen = turtle.Screen()
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
allStates = data.state.to_list()
guessedStates = []

while len(guessedStates) < 50:
    answerState = screen.textinput(title=f"{len(guessedStates)}/50 states correct", prompt="What's another state's name?").title()

    if answerState == "Exit":
        break
    if answerState in allStates:
        guessedStates.append(answerState)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateData = data[data.state == answerState]
        t.goto(int(stateData.x), int(stateData.y))
        t.write(answerState)

statesToLearn = set(allStates).difference(guessedStates)
newData = pandas.DataFrame(statesToLearn)
print(newData)





