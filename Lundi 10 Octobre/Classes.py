class MyClass:
    pass

print(MyClass, MyClass())

class PositionnalClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

var = PositionnalClass(2,3)
print(PositionnalClass, var, var.a, var.b)

class PositionnalClass2:
    def __init__(self, col=5, line=4):
        self.col = col
        self.line = line
var2 = PositionnalClass2( 2, col = 6)
print(var2.col, var2.line)