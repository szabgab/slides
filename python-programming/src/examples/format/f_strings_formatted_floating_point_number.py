val = 412.345678901

print(f"{val:e}")   #  exponent:     4.123457e+02
print(f"{val:E}")   #  Exponent:     4.123457E+02
print(f"{val:f}")   #  fixed point:  412.345679 (default precision is 6)
print(f"{val:.2f}") #  fixed point:  412.35 (set precision to 2)
print(f"{val:F}")   #  same as f.    412.345679
print(f"{val:g}")   #  generic:      412.346    (default precision is 6)
print(f"{val:G}")   #  generic:      412.346
print(f"{val:n}")   #  number:       412.346


print(f"{val}")     # defaults to g  412.345678901

