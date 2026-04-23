import math
from decimal import Decimal

print("\nFor all positive integers n, n! <= n²")
print("What is the limit we can reach within a certain range, so that became false?\n")

n=3
nrange = int(input("Insert Range: "))
varshow = input("Show math? (Y/N): ")
decimalrange = Decimal(1) / (Decimal(10) ** nrange)

while True:
    if math.gamma(n + 1) < (n ** 2):
        if varshow == "Y":
            print(f"\nFactorial of {n}: {math.gamma(n + 1):.{nrange}f}")
            print(f"{n} squared: {n ** 2:.{nrange}f}\n")
            n = round(n, nrange)
            n += decimalrange
        else:
            n = round(n, nrange)
            n += decimalrange

    else:
        n = round(n, nrange)
        print(f"Rupture point: {n}")
        print(f"Approximate factorial: {math.gamma(n + 1)}")
        print(f"Squared: {n ** 2}")
        break















