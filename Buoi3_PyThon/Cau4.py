x, y, z = 3, 5, 7

print("(a)", x == 3)                # True
print("(b)", x < y)                 # True
print("(c)", x >= y)                # False
print("(d)", x <= y)                # True
print("(e)", x != y - 2)            # False
print("(f)", x < 10)                # True
print("(g)", x >= 0 and x < 10)     # True
print("(h)", x < 0 and x < 10)      # False
print("(i)", x >= 0 and x < 2)      # False
print("(j)", x < 0 or x < 10)       # True
print("(k)", x > 0 or x < 10)       # True
print("(l)", x < 0 or x > 10)       # False