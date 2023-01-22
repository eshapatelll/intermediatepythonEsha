
res = 0

for i in range(5):
    while True:
        try:
            num = int(input("Enter an integer: "))
            res += num
            break
        except ValueError:
            print("Invalid input. Please enter an int.")

print("The sum is:", res)
