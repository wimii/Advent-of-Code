#Task 1
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


#Task 2
file = open("day1.txt", "r")
lines = file.readlines()
answer = 0
x = 0
for i in lines:
    print(i)
    li = []
    i = i.replace("one", "o1e")
    i = i.replace("two", "t2o")
    i = i.replace("three", "t3e")
    i = i.replace("four", "f4r")
    i = i.replace("five", "f5e")
    i = i.replace("six", "s6x")
    i = i.replace("seven", "s7n")
    i = i.replace("eight", "e8t")
    i = i.replace("nine", "n9e")
    print(i)
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