import math
radiuss = int(input("ievadi radiusu "))

while radiuss <= 0:
    radiuss = int(input("ievadi radiusu "))

L = 2 * math.pi * radiuss

print(L) 