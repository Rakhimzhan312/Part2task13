a = int(input('Введите число:'))
number = 0
for i in range(1, a + 1):
    i = i**2
    if i < a:
        print(i)
    