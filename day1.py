file = open("day1.txt", "r")
lines = file.readlines()
answer = 0
x = 0
for i in lines:
    print(i)
    li = []
    for chr in i:
        if chr.isdigit():
            li.append(chr)


    length = len(li)
    if length == 1:
        print (int(li[0] + li[0]))
        answer += int(li[0] + li[0])
    elif length == 2:
        print (int(li[0] + li[1]))
        answer += int(li[0] + li[1])
    else:
        print (int(li[0] + li[-1]))
        answer += int(li[0] + li[-1])

    print (answer)


print('Antwort', answer)

file.close()


