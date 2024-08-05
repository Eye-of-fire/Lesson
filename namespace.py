a = 5
b = 10
print(a,b)

def printer():
    global a,b
    a = 'str0'
    b = 'str1'
    c = 15
    d = 20
    print(c,d,"local")
    print(a,b,"global funks")

printer()
print(a,b,"global private funks")
