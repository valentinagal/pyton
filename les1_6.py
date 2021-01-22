a = int(input("Сколько км пробежал спортсмен?"))
b = a + (a * 0.1)
while b < a:
    b = a + (a * 0.1)
    if b == a:
        print()
