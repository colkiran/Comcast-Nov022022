
def outerFun(cname):
    info = f"Mr. {cname}"

    def innerFun():

        print("hello world")
        # print(f"Greetings {cname}")
        print(f"Greetings {info}")

    innerFun()


outerFun("Smith")

