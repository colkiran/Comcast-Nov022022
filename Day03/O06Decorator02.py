
def Pos_res(fnc):

    def helperFun(a, b):
        
        if b > a:
            a, b = b, a
        print(fnc(a, b))

    return helperFun


@Pos_res
def diff(x, y):
    return x - y


diff(10, 20)

print("-" * 40)

diff(20, 5)

print("-" * 40)

diff(5, 20)
