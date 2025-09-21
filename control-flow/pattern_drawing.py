size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    row += 1
    for num in range(size):
        print("*", end="")
    print() 
