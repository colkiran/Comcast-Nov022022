# this decorator is to calculate the total time taken by a function to execute
import time

def OuterFun(fnc):
    def helper(mx):
        st = time.perf_counter()
        fnc(mx)
        et = time.perf_counter()
        print(f"total time :{et - st}")
    return helper

@OuterFun
def fun(max):
    l = []
    for i in range(1, max):
        for j in range(1, i+1):
            l.append(i ** 2)

fun(6500)