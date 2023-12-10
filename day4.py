file = open("day4.txt", "r")
lines = file.readlines()
file.close()
for line in lines:
    print(line[10:39])