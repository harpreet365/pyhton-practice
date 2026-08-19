class Fib:

  def __init__(self, n):
    self.n = n
    self.a = 0
    self.b = 1

  def __iter__(self):
    return self

  def __next__(self):
    if self.n <= 0:
      raise StopIteration
    result = self.a
    self.a, self.b = self.b, self.a + self.b
    self.n -= 1
    return result


n_terms = int(input("Enter the number of terms: "))
for num in Fib(n_terms):
  print(num)
