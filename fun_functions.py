import math

# x = 10
new_var = 10

def test_funktion():
    y = 5
    x = math.sqrt(9)
    print(x)
    print(y)
    variabel = 'Något!'
    # Advanced
    def func2():
        print(x)
        print(new_var)
        # print(hej)

    func2()
    
    # att returnera funktioner är rätt avancerat...
    return list((variabel,x,func2))


t = test_funktion()
func2 = t[2]
print(t[0])
print(t[1])
func2()
t[0] = 10
print(f"{type(t)=}")