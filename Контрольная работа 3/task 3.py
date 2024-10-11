#1 задание множества и словари
n = int(input())
m = int(input())
manka = []
ovsyanka = []
for i in range(n):
    manka.append(input())
for i in range(m):
    ovsyanka.append(input())
manka = set(manka)
ovsyanka = set(ovsyanka)
all_kasha = manka.intersection(ovsyanka)
if len(all_kasha) == 0:
    print('Таких нет')
else:
    print(len(all_kasha))