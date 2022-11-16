
glbX = 100              # global variable

def fun(n):             # n is a local variable
    global glbX
    print(f"n :{n}")
    a = "Hello World"
    print(f"a :{a}")
    glbX = 500
    print(f"Inside glbX :{glbX}")


print(f"Before glbX :{glbX}")

fun(10)

print(f"After glbX :{glbX}")
