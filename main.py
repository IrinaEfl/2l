pas=input('введите пароль')
if len(pas)<5:
    print("короткий пароль")
elif pas[0:6] == "qwerty":
    print('ненадёжный пароль')
else:
    print("ок")

n=int(input('введите номер места'))
print()
if n>36:
    print('боковое')
elif n % 2:
    print('в купе внизу')
else:
    print('в купе вверху')

year=int(input())
if(year % 4 == 0) and (year % 100 != 0) and(year % 400 == 0):
    print('високосный')
else:
    print('не високосный')

colors = ('красный', 'синий','жёлтый')
с1 = input()
c2 = input()
if c1 in colors and c2 in colors:
    if c1 != c2:
        if (c1 in ('красный','синий')) and (c2 in ('красный','синий')):
            print('фиолетовый')
        if (c1 in ('красный','жёлтый')) and (c2 in ('красный','жёлтый')):
            print('оранжевый')
        if (c1 in ('жёлтый','синий')) and (c2 in ('жёлтый','синий')):
            print('зелёный')
    else:
        print(c1)
else:
    print('ошибка')

n = int(input("ввод кол слов: "))
result = " "
for i in range(n):
    w = input(f"ввод слов {i+1}:")
    result += w + " "
print("результат:", result.strip() )
