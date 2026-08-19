print("A5.6")
num = int(input("Enter a number: "))
s = str(num)
power = len(s)

total = sum(int(digit) ** power for digit in s)

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
