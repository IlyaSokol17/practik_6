x = int(input())
k = 0
for a in range(50):
    for b in range(50):
        if 5 * a + 7 * b == x:
            k += 1
if k >= 1:
    print('да')
else:
    print('нет')
