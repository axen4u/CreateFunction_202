def print_odd_numbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)

n = int(input("Enter the value of n: "))
print("Odd numbers up to", n, ":")
print_odd_numbers(n)