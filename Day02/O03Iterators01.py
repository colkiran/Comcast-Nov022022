
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")
print(type(l))

print("-" *  40)
# print(dir(l))
iterObj = l.__iter__()             # dunder iter method => double underscore
print(dir(iterObj))

# __next__ and __iter__ method are the protocols of iteration

print("-" *  40)
elem01 = iterObj.__next__()
print(elem01)

print("-" *  40)
elem02 = iterObj.__next__()
print(elem02)

print("-" *  40)
elem03 = next(iterObj)          # call __next__()
print(elem03)

print("-" *  40)
elem04 = next(iterObj)
print(elem04)

print("-" *  40)
elem05 = next(iterObj)
print(elem05)

# print("-" *  40)
# elem06 = next(iterObj)
# print(elem06)

print("-" *  40)
for i in l:
    print(i, end=" ")
print()
