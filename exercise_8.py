a = []
for i in range(0, 10):
        a.append(i)
for i in range(10, 100):
        a.append(i//10)
        a.append(i%10)
for i in range (100, 201):
        a.append(i//100)
        a.append((i%100)//10)
        a.append(i%10)

print(a)
x = int(input())
print(a[x - 1])
