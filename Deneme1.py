
# Online Python - IDE, Editor, Compiler, Interpreter

def quad1(a, b, c):
    determ=(b*b-4*a*c)**0.5
    x=(-b+determ)/(2*a)
    return x

def quad2(a, b, c):
    determ=(b*b-4*a*c)**0.5
    x=(-b-determ)/(2*a)
    return x
    
def print_x(a, b, c):
    print("The x1 value is",quad1(a, b, c))
    print(",and the x2 value is",quad2(a, b, c))
    
print_x(1,-1,-1)