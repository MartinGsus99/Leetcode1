# Python @ 函数装饰器用法

def funA(fn):
    print("This is FunA1")
    fn()
    print("This is FunA2")
    return "装饰器函数的返回值"

@funA
def funB():
    #...
    print("This is funB.")

print(funB)