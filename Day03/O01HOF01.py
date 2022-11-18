
def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def log_details(fnc):
    logInfo = "Logging into the service....."

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))                   # call back
        print("-" * 40)

    return innerFun

sum_logger = log_details(sum)
sum_logger(45, 95)

diff_logger = log_details(diff)
diff_logger(85, 30)
