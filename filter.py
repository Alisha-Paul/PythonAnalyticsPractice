#numbers = [-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
#  15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#less_than_zero = list(filter(lambda x: x < 0, numbers))
#print(less_than_zero)

from functools import reduce
print (reduce( (lambda x, y: x * y), [1, 2, 3, 4] ))
