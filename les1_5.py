a = int(input("Какая у вас была выручка? "))
b = int(input("А какие были издержки? "))
stuff = int(input("Сколько сотрудников у вас в фирме?"))
income = a - b
rent = income / a
perperson = income / stuff
if a < b:
    print("Ваша фирма терпит убытки")
else:
    print("Ваша фирма отработала с прибылью!")
print("Рентабельность вышей выручки:", rent, "%")
print("В расчете на одного сотрудника прибыль в фирме:", perperson)
