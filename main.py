# Matthew Delgado
# ECE 3541: Digital State Machines
# Module 1: Finite State Machines
# 09/21/2022

# import StateMachine.py file
from StateMachine import StateMachine

# adjective lists
positive_adj = ["great","super", "fun", "entertaining", "easy"]
negative_adj = ["boring", "difficult", "ugly", "bad"]

# Check the argument for the correct transition function value.
# if transition to "Python State" return newState
# else return "Error state" and the input "txt"
def start_transitions(txt):
    split_txt = txt.split(None, 1)
    word, txt = split_txt if len(split_txt) > 1 else (txt,"")
    if word == "Python":
        newState = "Python_state"
    else:
        newState = "error_state"
    return (newState, txt)

# Check the argument for the correct state indicator "is" value.
# if the value equals "is" set newState to "is_state"
# else set newState equals “error_state”
# function should return newState and the input "txt"
def python_state_transitions(txt):
    split_txt = txt.split(None, 1)
    word, txt = split_txt if len(split_txt) > 1 else (txt,"")
    if word == "is":
        newState = "is_state"
    else:
        newState = "error_state"
    return (newState, txt)

# Check the argument for the correct state transition
# “not, pos_state, neg_state” value.
# if the value equals "not" set newState to "not_state"
# if the value is in "positive_adj" set newState to "pos_state"
# if the value is in "negative_adj" set newState to "neg_state"
# else set newState equals “error_state”
# function should return newState and the input "txt"
def is_state_transitions(txt):
    split_txt = txt.split(None, 1)
    word, txt = split_txt if len(split_txt) > 1 else (txt,"")
    if word == "not":
        newState = "not_state"
    elif word in positive_adj:
        newState = "pos_state"
    elif word in negative_adj:
        newState = "neg_state"
    else:
        newState = "error_state"
    return (newState, txt)

# Check the argument for the "not a state transition"
# if the value is in "positive_adj" set newState to "neg_state"
# if the value is in "negative_adj" set newState to "pos_state"
# else set newState equals “error_state”
# function should return newState and the input "txt"
def not_state_transitions(txt):
    split_txt = txt.split(None, 1)
    word, txt = split_txt if len(split_txt) > 1 else (txt,"")
    if word in positive_adj:
        newState = "neg_state"
    elif word in negative_adj:
        newState = "pos_state"
    else:
        newState = "error_state"
    return (newState, txt)

# declare new object m
m = StateMachine()
# add states
m.add_state("Start", start_transitions)
m.add_state("Python_state", python_state_transitions)
m.add_state("is_state", is_state_transitions)
m.add_state("not_state", not_state_transitions)
m.add_state("neg_state", None, end_state = 1)
m.add_state("pos_state", None, end_state = 1)
m.add_state("error_state", None, end_state = 1)
# set starting state
m.set_start("Start")
# run tests
m.run("Python is great")
m.run("Python is difficult")
m.run("Perl is ugly")