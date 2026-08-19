print("A5.20 -------character with ASCII in decimal, binary,hex,and oct(0-255)")
print(f"{'Dec':<6} {'Oct':<6} {'Hex':<6} {'Binary':<12} {'Char'}")
print("-" * 40)
for i in range(256):
    print(f"{i:<6} {oct(i)[2:]:<6} {hex(i)[2:].upper():<6} {bin(i)[2:]:>08}   {chr(i)!r}")
