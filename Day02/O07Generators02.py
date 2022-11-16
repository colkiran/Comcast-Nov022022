
def fun():
    n = 1
    print("apples from ooty....")
    yield n
    n += 9
    print("oranges from kanpur.....")
    yield n
    n += 10
    print("grapes from hubli.....")
    yield n

res = fun()
print(res)
print(type(res))

print("-" *  40)
print(res.__next__())

print("-" *  40)
print(res.__next__())

print("-" *  40)
print(res.__next__())

# print("-" *  40)
# print(res.__next__())

print("-" *  40)
def fun1():
    for i in range(1, 11):
        yield i

gen = fun1()
print(next(gen))

print("-" *  40)
print(next(gen))

print("-" *  40)
for x in fun1():
    print(x, end=" ")
print()
