op = [3, -2, -3, 51, 31]

for i in range(0,4):
    temp = 0
    temp2 = 0
    if op[i] > op[1+i]:
        temp = op[i]
        temp2 = op[1+i]
        op[i] = temp2
        op[1+i] = temp


print(op)