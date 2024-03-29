n = input('введите путь коня(например: d3-e5): ').lower()
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n_1 = int(n[4])
n_2 = int(n[1])
if abs(n_2 - n_1) == 2:
    c = a.index(n[0])
    if a[c + 1] == n[3] or a[c - 1] == n[3]:
        print('верно')
    else:
        print('ошибка')
elif abs(n_1 - n_2) == 1:
    c = a.index(n[0])
    if a[c + 2] == n[3] or a[c - 2] == n[3]:
        print('верно')
    else:
        print('ошибка')
else:
    print('ошибка')