
def outerFun(cname):                    # HOF - higher order function
    info = f"Mr. {cname}"

    def innerFun():

        print("hello world")
        # print(f"Greetings {cname}")
        print(f"Greetings {info}")

    return innerFun


infun = outerFun("Smith")
print("after few lines of code")
print("-" * 40)

infun()

print("-" * 40)
print(outerFun.__name__)
print(outerFun("abc").__name__)