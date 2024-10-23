import random, re

len_spisok = random.randint(10, 100)
spisok = [random.randint(-100000, 100001) for _ in range(len_spisok)]
#^\d{4}3$
pattern = r'^\d{4}3$'
max_element = 0
for i in spisok:
    if i > max_element and re.match(pattern, str(i)):
        max_element = i
counter = 0
for i in range(2, len_spisok):
    if (spisok[i-2] % 10 == 3 or spisok[i-1] % 10 == 3 or spisok[i] % 10 == 3) and spisok[i]+spisok[i-1]+spisok[i-2] <= max_element:
        counter += 1
print(counter)

