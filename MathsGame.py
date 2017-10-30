#!/usr/bin/env python


import random
import easygui

points = 0


def r():
    global points
    symbol_random = random.randint(1, 3)
    answer = 0
    symbol = 0

    if symbol_random == 1:
        no_1 = random.randint(5, 25.0)
        no_2 = random.randint(5, 25.0)
        answer = no_1 + no_2
        symbol = "+"

    if symbol_random == 2:
        no_1 = random.randint(5, 25.0)
        no_2 = random.randint(5, 25.0)
        answer = no_1 - no_2
        symbol = "-"

    if symbol_random == 3:
        no_1 = random.randint(5, 12.0)
        no_2 = random.randint(5, 12.0)
        answer = no_1 * no_2
        symbol = "x"

    random_button = random.randint(1, 3)
    random_button_no_ = random.randint(1, 5)
    if random_button == 1:
        input = easygui.buttonbox(str(no_1) + str(symbol) + str(no_2) + "=",
                                  "points: " + str(points),
                                  choices=[str(answer),
                                           str(answer + random_button_no_),
                                           str(answer - random_button_no_)])
    if random_button == 2:
        input = easygui.buttonbox(str(no_1) + str(symbol) + str(no_2) + "=",
                                  "points: " + str(points),
                                  choices=[str(answer - random_button_no_),
                                           str(answer + random_button_no_),
                                           str(answer)])
    if random_button == 3:
        input = easygui.buttonbox(str(no_1) + str(symbol) + str(no_2) + "=",
                                  "points: " + str(points),
                                  choices=[str(answer + random_button_no_),
                                           str(answer),
                                           str(answer - random_button_no_)])

    if float(input) == float(answer):
        points = points + 5
        return easygui.buttonbox(("Correct!"),
                                 choices=['[OK]', '[EXIT]'])
    if float(input) != float(answer):
        points = points - 2
        return easygui.buttonbox(("Wrong!\nIt is " + str(answer)),
                                 choices=['[OK]', '[EXIT]'])

while True:
    response = r()
    if str(response) == '[EXIT]':
        break
