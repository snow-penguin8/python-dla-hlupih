import random

plys = [
        "ph",
         0,
         0
]

itog = [
    "ph3",
    "блубжижник",
    "ножницы",
    "бумага"
]
x = True
while (x):

    try:
        plys[1] = int(input("Введи число от 1 - 3:"))
        if plys[1] in [1, 2, 3]:
            break
        else:
            print("число от 1-3")
    except ValueError:
        print("^gugu gaga is here^")
        x = True

def pov(x):

    if x == 1:
        print(itog[1])
    elif x == 2:
        print(itog[2])
    elif x == 3:
        print(itog[3])
    else:
        print("Введено неверное значение")
    pass

pov(plys[1])

plys[2] = random.randint(1, 3)

pov(plys[2])


# def po2v():
#
#     if plys[2] == 1:
#         print(itog[1])
#     elif plys[2] == 2:
#         print(itog[2])
#     elif plys[2] == 3:
#         print(itog[3])
#     else:
#         print("Введено неверное значение")
#
# pass

if plys[1] == 1 and plys[2] == 2 or plys[1] == 2 and plys[2] == 3 or plys[1] == 3 and plys[2] == 1:
        print("ты подебил!")
elif plys[1] == 1 and plys[2] == 3  or plys[1] == 2 and plys[2] == 1 or plys[1] == 2 and plys[2] == 1 or plys[1] == 3 and plys[2] == 2:
    print("ты проиграл")
else:
    print("ничья")


#
# winlose = {
#     (1,2): "ты подебил!",
#     (2,3): "ты подебил!",
#     (3,1): "ты подебил!",
#     (1,3):"ты проиграл",
#     (2,1):"ты проиграл",
#     (3,2):"ты проиграл"
# }
#
# if plys[1] == plys[2]:
#         print("ничья")
# else:
#     result = winlose.get((plys[1], plys[2]))
#     print(result)