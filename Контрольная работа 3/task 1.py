#1 задание списки
n, m = map(int, input().split())
massive = []
for i in range(n):
    massive.append([])
    if i % 2 == 0:
        for j in range(m*i, m*(i+1)):
            massive[i].append(j)
    else:
        for j in range(m*(i+1)-1, m*(i)-1, -1):
            massive[i].append(j)
for i in massive:
    print(*i)