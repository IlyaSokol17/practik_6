a, b = input('введите размер отверстия(AxB):').split('x')
c, d, e = input('введите размер кирпича').split('x')
if (((c <= a) and (d <= b)) or ((d <= a) and (c <= b))
    or ((c <= a) and (e <= b)) or ((e <= a) and (c <= b)) or
    ((d <= a) and (e <= b)) or ((e <= a) and (d <= b))) :
    print('Кирпич влезает')
else:
    print('кирпич не влезает')