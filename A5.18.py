print("A5.18----print and count leap year btw 2021-2026")
count = 0
print("Leap Years between 2021 and 2026:")
for year in range(2021, 2027):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
        count += 1

print(f"Total leap years: {count}")
