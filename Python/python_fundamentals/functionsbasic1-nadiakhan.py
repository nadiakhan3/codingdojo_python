def a():
    return 5
print(a())
#output is 5

def a():
    return 5
print(a()+a())
#output is 5+5

def a():
    return 5
    return 10
print(a())
#output is 5 doesn't return 10 because function ends after return

def a():
    return 5
    print(10)
print(a())
#output would be 5 function ends after return value

def a():
    print(5)
x = a()
print(x)
#output would be 5

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#output would be 3 and 5


