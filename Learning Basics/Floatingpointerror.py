# Python has issues with floating point arithmetic which leads to rounding errors, loss of precision
# Floating point error occurs because, Floating-point errors arise because computers store real numbers using a finite number of bits, leading to approximations and potential inaccuracies.

# Below program will show an example where the floating point error can be seen

decimal = 99999.9
binary = format(decimal, '.20f')  # 20 decimal places
print(f"Decimal: {decimal}\nBinary: {binary}")

# With the above program we can clearly see 99999.90 becomes 99999.89 due to floating point error in python.
