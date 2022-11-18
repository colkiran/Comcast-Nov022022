
def funLogger(fnc):
    def helper():
        print("My info logged into a service")
        fnc()
        print("My info logger channel closed.....")

    return helper

def normalfun():
    print("I should be called as normal")

funLogger(normalfun)

print("-" * 40)

funLogger(normalfun)()

print("-" * 40)

res_fun = funLogger(normalfun)
res_fun()

print("-" * 40)

normalfun = funLogger(normalfun)
normalfun()

print("-" * 40)

@funLogger                              # decorator
def basicFun():
    print("I should be called as Basic")

basicFun()