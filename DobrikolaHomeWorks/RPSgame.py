from random import choice

player = ["камень", "ножницы", "бумага"]
x = True
while (x):
    bot = ["камень", "ножницы", "бумага"]
    print("введи значение")
    a = (str(input()))
    if a in player:
         break
    else:
          continue

bot = choice(bot)
print(f"bot:{bot}")

if a == bot :
    print("ничья")
elif ((a == "камень" and bot == "ножницы")
      or (a == "ножницы" and bot == "бумага")
      or (a == "бумага" and bot == "ножницы")):
    print("ты победил")
else:
    print("бот победил")