
def outerFun(cname):

    def innerFun():
        nonlocal cname           # only local variable can be converted into                            nonlocal
        cname = "Mike"
        print("Hello World.....")
        print(f"greetings {cname}")

    innerFun()
    print(f"After :{cname}")


outerFun("Rahul")
