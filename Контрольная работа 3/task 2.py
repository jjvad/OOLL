#2 задание списки
n, m = map(int, input().split())
massive = []
for i in range(n):
    massive.append(list(map(int, input().split())))
print(m, n)
for i in range(m):
    for j in range(n-1, -1, -1):
        print(massive[j][i], end=' ')
    print()
