numbers = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
               [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

rnum = len(numbers)
cnum = len(numbers[0])
numCross = 0

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] == 1:
            if i != len(numbers[i])-1 and j != len(numbers)-1:
                if numbers[i-1][j] == 1 and numbers[i+1][j] == 1 and numbers[i][j-1] == 1 and numbers[i][j+1] == 1:
                    numCross += 1
                    print("(" + str(j+1) + ", " + str(i+1) + ")")

print(numCross)