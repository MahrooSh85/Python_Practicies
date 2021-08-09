# Define a function which does summation of its inputs

def f(*args):
    s = 0
    for i in args:
        s = s + i
    return s


print(f(5, 2))
print(f(5, 2, 11, 3, 10))


