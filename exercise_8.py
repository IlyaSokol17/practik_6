a = []
for i in range(0, 201):
    if i < 10:
        a.append(i)
    if i >=10 and i <= 99:
        a.append(i//10)
        a.append(i%10)
    if i>=100:
        a.append(i//100)
        a.append((i%100)//10)
        a.append(i%10)

print(a)
x = int(input())
print(a[x])
