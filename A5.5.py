print("A5.4")
n = int(input("Enter a Number: "))
original = n
reversed_n = 0
while n > 0:
    digit = n % 10
    digit = n % 10 + digit
    n =n // 10
if original == reversed_n:
    print("Palindrome")
else:
    print("Not a Pallindome")
