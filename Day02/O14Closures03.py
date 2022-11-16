
def outerFun(greet):
    def innerFun(gname):
        print(greet, gname)
    return innerFun

# simple currry
engGrt = outerFun("Welcome")
engGrt("Sachin")

hndGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakam")


engGrt("Messi")
engGrt("Fedrer")

print("-" * 40)
hndGrt("Virat")

print("-" * 40)
tmlGrt("Natraj")

