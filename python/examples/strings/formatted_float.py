x = 412.345678901

print("{:e}".format(x)) #  exponent:     4.123457e+02
print("{:E}".format(x)) #  Exponent:     4.123457E+02
print("{:f}".format(x)) #  fixed point:  412.345679 (default precision is 6)
print("{:F}".format(x)) #  same as f.    412.345679
print("{:g}".format(x)) #  generic:      412.346    (default precision is 6)
print("{:G}".format(x)) #  generic:      412.346
print("{:n}".format(x)) #  number:       4412.346


print("{}".format(x))   # defaults to g  412.345678901
