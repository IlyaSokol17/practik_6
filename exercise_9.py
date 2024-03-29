import turtle
x, y, r_1 = map(int, input('введите координаты и радиус превого круга').split())
z, c, r_2 = map(int, input('введите координаты и радиус второго круга').split())

turtle.up()
turtle.setposition(x, y - r_1)
turtle.pensize(1)
turtle.pencolor('red')
turtle.down()
turtle.circle(r_1)
turtle.up()
turtle.goto(z, c - r_2)
turtle.down()
turtle.circle(r_2)
d = ((x - z) ** 2 + (y - c) ** 2) ** 0.5
print(d)
if r_1 + r_2 == d :
    print('Окружности имеют внешнее касание')
if abs(r_1 - r_2) == d:
    print('окружности имеют внутреннее касание')
if abs(r_1 -r_2) > d:
    print('одна окружность лежит внутри  другой не касаясь')
if r_1 + r_2 < d:
    print('окружности лежат одна вне другой, не касаясь')
if (r_1 + r_2 - abs(r_1 - r_2)) == d:
    print('окружности пересекаются')
turtle.done()