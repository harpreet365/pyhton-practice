# yieldfibo.py
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


num_terms = int(input("Enter the number of terms: "))

for num in fibonacci(num_terms):
    print(num)