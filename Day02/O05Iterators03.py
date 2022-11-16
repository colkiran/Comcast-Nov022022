
class Mynumbers:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            res = self.n
            self.n += 1
            return res
        else:
            raise StopIteration

mynum = Mynumbers(10)
iterObj = iter(mynum)

e1 = iterObj.__next__()
print(e1)

e2 = iterObj.__next__()
print(e2)

e3 = iterObj.__next__()
print(e3)

e4 = iterObj.__next__()
print(e4)

e5 = iterObj.__next__()
print(e5)

# e6 = iterObj.__next__()
# print(e6)

for i in mynum:
    print(i, end=" ")
print()
