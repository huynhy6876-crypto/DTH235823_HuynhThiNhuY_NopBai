n = int(input("Nhập n: "))

# Hình 1: hình vuông rỗng
print("\nHình 1:")
for i in range(n):
    line = ""
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            line += "* "
        else:
            line += "  "
    print(line)
# Hình 2: hình tam giác vuông
print("\nHình 2:")
print(" " * 5 + "*" );
print(" " * 4 + "**");
print(" " * 3 + "***");
print(" " * 2 + "****");


