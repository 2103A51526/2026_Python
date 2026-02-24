a = int(input("Enter a number "))
for i in range(1, a+1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fuzzbuzz")
    elif i % 3 == 0:
        print("Fuzz")
    elif i % 5==0:
        print("Buzz")