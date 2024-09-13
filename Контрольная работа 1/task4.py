N = int(input())
zero_counter = 0
while N != 0:
    if N % 10 == 0:
        zero_counter += 1
    N //= 10
print(zero_counter)