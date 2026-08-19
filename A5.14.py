print("A5.14----sum of series(1**2/2+2**/2+3**2/2....")
n = int(input("Enter the value of n: "))
series_sum = sum((i ** 2) / i for i in range(1, n + 1))
print(f"Sum of the series: {series_sum}")
