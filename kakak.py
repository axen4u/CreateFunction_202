def print_design(n):
    for i in range(1, n + 1):
        for _ in range(i):  # Replace "j" with "_"
            print(i, end=" ")
        print()

n = int(input("Enter the value of n: "))
print_design(n)
