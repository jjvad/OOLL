N = int(input())
factorial = 1
summa = 0
for i in range(1, N + 2):
    summa += 1/factorial
    factorial *= i
print(f"{summa:.5f}")