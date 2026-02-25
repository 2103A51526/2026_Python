a = int(input("Enter a number: "))
total = 0
if a % 2 != 0:
    for i in range(1, a + 1):
        total = total + i
print("The sum of all odd number is ", total)