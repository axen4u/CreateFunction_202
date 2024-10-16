def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):  # Replace "i" with "_"
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter the value of n: "))
print("Fibonacci series up to", n, ":", fibonacci(n))
