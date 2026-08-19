print("A5.13----sum of series(1/2+2/3....)")
n = int(input("Enter the value of n: "))
series_sum = sum(i / (i + 1) for i in range(1, n + 1))
print(f"Sum of the series: {series_sum:.4f}")
