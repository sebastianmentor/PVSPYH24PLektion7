#---------- Version 1 ------------
# x = 10

# def test_funktion():
#     y = 5
#     x = 5
#     print(x)
#     print(y)

# test_funktion()
# print(x)

#---------- Version 2 ------------
# x = 10

# def test_funktion():
#     y = 5
#     print(x)
#     x = 2
#     print(y)

# test_funktion()
# print(x)

#---------- Version 3 ------------
x = 10
glob_tuple = (1,2,3)
super_lists = [1,2,3]

def test_funktion(glob_list, glob_tuple):
    y = 5
    global x
    print(glob_tuple)
    # glob_tuple[0] = 10
    print(glob_list)
    glob_list[0] = 10
    print(glob_list)
    print(x)
    x = 2
    print(y)

test_funktion(super_lists, glob_tuple)
print(super_lists)
print(x)