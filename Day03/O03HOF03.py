
def greet(msg):
    print(msg)

greet("Welcome")

fun_name = greet

print(fun_name.__name__)
print(greet.__name__)

fun_name("hello")

print("-" * 40)

def bank_flow(fnc):     #HOF
    print("-" * 40)
    print("login")
    fnc()               # callback
    print("logout")
    print("-" * 40)


def withdraw():
    print("debited from the account......")

def deposit():
    print("credited into the account.......")

bank_flow(withdraw)
bank_flow(deposit)