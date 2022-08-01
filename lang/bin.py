a,b = 1.0, 2.0
n = 2

while True:
    c = (a+b)/2
    if abs(c*c - n) < 0.00000001:
        print(c)
        break
    if c*c < n:
        a = c
    else:
        b = c

