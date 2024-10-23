import re

data_string = input()

pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/((1[6-9])[0-9]{2}|[2-9][0-9]{3})$"

if re.match(pattern, data_string):
    day_in_string, month_in_string, year_in_string = map(int, data_string.split('/'))
    days_in_month = [31, 29 if year_in_string % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= day_in_string <= days_in_month[month_in_string-1]:
        print(True)
    else:
        print(False)
else:
    print(False)