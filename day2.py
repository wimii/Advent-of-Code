# Task 1
import re

file = open("day2.txt", "r")
lines = file.readlines()
file.close()
answer = 0
red = 12
green = 13
blue = 14

for line in lines:
    game = ''.join(re.findall(r'\d\d?\d?:', line))
    game = game[:-1]
    good = 1

    cols = re.findall(r'\d+ ...?.?.', line)

    for col in cols:
        if 'red' in col:
            r = ''.join(re.findall(r'\d?\d', col))
            if int(r) > red or not good:
                good = 0
                break

        if 'green' in col or not good:
            g = ''.join(re.findall(r'\d?\d', col))
            if int(g) > green:
                good = 0
                break

        if 'blue' in col or not good:
            b = ''.join(re.findall(r'\d?\d', col))
            if int(b) > blue:
                good = 0
                break

    if good:
        answer += int(game)

print("final answer task 1", answer)

# Task 2

import re

file = open("day2.txt", "r")
lines = file.readlines()
file.close()
answer = 0
red = 0
green = 0
blue = 0

for line in lines:
    game = ''.join(re.findall(r'\d\d?\d?:', line))
    game = game[:-1]

    cols = re.findall(r'\d+ ...?.?.', line)

    for col in cols:
        if 'red' in col:
            r = ''.join(re.findall(r'\d?\d', col))
            if int(r) > red:
                red = int(r)

        if 'green' in col:
            g = ''.join(re.findall(r'\d?\d', col))
            if int(g) > green:
                green = int(g)

        if 'blue' in col:
            b = ''.join(re.findall(r'\d?\d', col))
            if int(b) > blue:
                blue = int(b)

    answer = answer + red * green * blue

    red = 0
    green = 0
    blue = 0

print("final answer task 2", answer)
