""""#Task 1
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
    print("game ", game)
    good = 1

    cols = re.findall(r'\d+ ...?.?.', line)

    print(cols)

    for col in cols:
        if 'red' in col:
            r = ''.join(re.findall(r'\d?\d', col))
            if int(r) > red or not good:
                good = 0
                print("Too much red", r)
                break

        if 'green' in col or not good:
            g = ''.join(re.findall(r'\d?\d', col))
            if int(g) > green:
                good = 0
                print("Too much green", g)
                break

        if 'blue' in col or not good:
            b = ''.join(re.findall(r'\d?\d', col))
            if int(b) > blue:
                good = 0
                print("Too much blue", b)
                break

    if good:
        answer += int(game)

    print("answer:", answer)



print("final answer", answer)

"""