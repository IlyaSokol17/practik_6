x, y, c, a  = map(int, input('введите координаты верхней левой вершины(x, y) и правой нижней вершины(c, a)'
                      ' первого прямоугольника').split())
w, z, b, d = map(int, input('введите координаты верхней левой вершины(w, z) и правой нижней вершины(b, d)'
                      ' второго прямоугольника').split())
r_1 = y - a #вертикаль
r_2 = c - x #горизонталь

n_1 = z - a #вертикаль
n_2 = b - w #горизонталь

#if ((x < w and y > z) and (c < b and a > d)) or ((w < x and z > y) and (b > c and d > a)):
if (((b > x and b < c and a < d < y) and (x < w < c and a < z < y)) or ((x < b < c and a < z < y) and (x < w < c and y < d < a)) ):
    print('один прямоугольник лежит внутри другого не касаясь')
if (y - r_1 > z) or (c - r_2 > b) or (z - n_1 > y)  or (b - n_2 > c):
    print('прямоугольникик лежат вне друг друга, не касаясь ')
if (((c >= w and c <= b and a == z) or ((c -r_2 <=b and c - r_2 >= w and a == z))) or
    ((((y - r_1) <= a and (y - r_1) >= d  and x == b  )) or ((y <= a and y >= d   and x == b)))  or
    ((y == d and x <= b and x >= w) or ((x + r_2) <= b and y == d and (x + r_2 >= w))) or
    ((y >= d and y <= z and c == w) or (a >= d and a <=z and c == w))):
    print('прямоугольники имеют касание')
if ((b > x and b < c and a < d < y) or (x < w < c and y < d < a) or
    (x < w < c and a < z < y) or (x < b < c and a < z < y)):
    print('Прямоугольники пересекаются')