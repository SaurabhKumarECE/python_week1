
print("\n---- Sum of N Numbers ----")
n = int(input("Enter N: "))

total = 0

# Using for loop
for i in range(1, n + 1):
    total += i

print("Sum using for loop:", total)

# Using while loop
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum using while loop:", total)
