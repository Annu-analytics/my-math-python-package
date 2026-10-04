# Advanced mathematical functions
def power(a,b):
  return a ** b
def square(n):
  return n ** 2
def cube(n):
  return n ** 3
def square_root(n):
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers")
    return n ** 0.5
def factorial(n):
  if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    

  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
