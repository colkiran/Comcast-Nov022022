
# what are lambdas?
# lambdas are anonymous function with a single expression

"""
exp_result = lambda var1, var2, var3....: expression
"""

def add(x, y):
    return x + y

a = add

res = a(15, 35)
print(f"res :{res}")

print("-" * 40)

b = lambda x, y: x + y
res = b(12, 42)
print(f"res :{res}")

# lambdas are best used with MAP, FILTER and REDUCE
# map => will map a list to an expression and implement the expression on every element of the list
l = list(range(1, 11))
print(f"l :{l}")

squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")
print("-" * 40)

months = ['dec', 'apr', 'aug', 'nov', 'mar', 'oct', 'feb', 'may', 'sep', 'jul', 'jan', 'jun']

# sort these months using map and lambda
from calendar import month_name
# print(list(month_name))
print(f"months :{months}")
res  = sorted(months, key=list(map(lambda mth: mth[0:3].lower(), list(month_name))).index, reverse=True)

print(f"res    :{res}")

print("-" * 40)
# filter => expression will return a True or False and will be implemented on every number in the list

l = list(range(1, 26))

print(f'l :{l}')
res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("-" * 40)
from functools import reduce

l = [7, 4, 8, 6, 9, 3, 10, 5]
print(f"l :{l}")
res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

print("-" * 40)

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")
