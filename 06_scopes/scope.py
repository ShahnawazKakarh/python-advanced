# This script demonstrates Python variable scopes

m = 99 # global scope

###############################################################

x = "global x"  # This is a global variable

###############################################################

def test():
    y = "local y"  # This is a local variable
    print(x)       # Accessing the global variable
    print(y)       # Accessing the local variable

test()
# print(y)  # This would raise an error because y is not defined in the global scope

###############################################################

def test2(y):
    z = m + y # m will be called here from global scope
    return z

result = test2(12)
print(result)

###############################################################

def func3():
    global x # this way is not recommended for calling global variable
    x = 12
    
func3()
print(x)

###############################################################

def f1():
    m=88 # if I comment it, it will print 99
    def f2():
        print(m)
    f2()
f1()

###############################################################
# Closure or Factory function

def f3():
    x = 88
    def f4():
        print(x)
    return f4
myResult = f3()
myResult()

###############################################################
# Example 2 of Closure or Factory function
def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))

###############################################################
