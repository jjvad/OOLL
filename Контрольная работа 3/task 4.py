#3 задание множества и словари
massive = list(map(int, input().split()))
repeats = set()
for i in massive:
    if i not in repeats:
        print('NO')
        repeats.add(i)
    else:
        print('YES')
        repeats.add(i)