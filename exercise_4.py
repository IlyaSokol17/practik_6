n = input('введите клетку шахматного поля: ').lower()
l_1 = ['a', 'c', 'e', 'g']
l_2 = ['b', 'd', 'f', 'h']

if n[0] in l_1:
    if int(n[1]) % 2 == 0:
        print('белый')
    else:
        print('черный')

if n[0] in l_2:
    if int(n[1]) % 2 == 0:
        print('черный')
    else:
        print('белый')
