
print("\n---- Prime Number Check ----")
num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True

    # Loop from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break   # break used here

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

