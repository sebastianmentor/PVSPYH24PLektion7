def mult(x,y):
    mult = x*y
    return mult

def add(x,y):
    add = x + y
    return add
    # return x + y <-- fungerar också

def add_and_mult(x,y,z,m):
    """
    Add x+y and z+m and multiply the result.
    """
    add1 = add(x,y)
    add2 = add(z,m)
    mul = mult(add1,add2)
    return mul

total = add(5, 8)
print(total)
print(mult(5,8))

total2 = add(5.5, 8.5)
print(total2)
print(mult(5.5,8.5))

print(mult(add(5,2), add(4,7)))
print(add_and_mult(5,2,4,7))
      
total3 = add('Hello', 'World')
print(mult('Hello',5))
print(mult(5,'Hello'))
print(total3)








def string_to_upper(text):
    return text.upper()

upper_case = string_to_upper('jag skriver med små bokstäver först')
print(upper_case)
