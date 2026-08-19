print("A5.19------print odd and even number side-by-side")
print(f"{'Odd No. between 1-100':<25} {'Even No. between 1-100':<25}")
print("-" * 50)
for i in range(1, 100, 2):
    print(f"{i:<25} {i + 1:<25}")
