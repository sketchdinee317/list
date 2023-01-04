def square_num(n):
  return n * n
x = [4, 5, 2, 9]
result = map(square_num, x)
print("Square the elements of  the list:")
print(list(result))

