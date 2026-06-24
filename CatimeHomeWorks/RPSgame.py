import random

plys = [
        "ph",
         0,
         0
]
choices = [
    "ph2",
    "камень",
    "ножницы",
    "бумага"
]
itog = [
    "ph3",
    "камень",
    "ножницы",
    "бумага"
]
x = True
while (x):

    try:
        plys[1] = int(input())
        if isinstance(plys[1], int):
            break
        else:
            continue
    except ValueError:
        print("^gugu gaga is here^")
        x = True

def pov():

    if plys[1] == 1:
        print(itog[1])
    elif plys[1] == 2:
        print(itog[2])
    elif plys[1] == 3:
        print(itog[3])
    else:
        print("Введено неверное значение")
pass

pov()

plys[2] = random.randint(1, 3)

def po2v():

    if plys[2] == 1:
        print(itog[1])
    elif plys[2] == 2:
        print(itog[2])
    elif plys[2] == 3:
        print(itog[3])
    else:
        print("Введено неверное значение")

pass

po2v()

if plys[1] == plys[2]:
        print("ничья")

if plys[1] == 1 and plys[2] == 2:
        print("ты подебил!")
if plys[1] == 3 and plys[2] == 1:
        print("ты подебил!")
if plys[1] == 2 and plys[2] == 3:
        print("ты подебил!")

if plys[1] == 1 and plys[2] == 3:
    print("ты проиграл")
if plys[1] == 2 and plys[2] == 1:
    print("ты проиграл")
if plys[1] == 3 and plys[2] == 2:
    print("ты проиграл")