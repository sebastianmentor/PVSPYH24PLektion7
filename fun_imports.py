#from if_name_eq_main import main
glob_dict = {}

def my_function():
    """
    The best function in the world!
    No arguments are needed!
    """
    print('Runs my_function')

def print_sträng_tal_number_of_times(tal,sträng):
    """
    Vi skriver ut en rolig text baserat på tal och sträng!
    """
    if type(tal) == int:
        print(tal*sträng)
    else:
        print("Går inte att köra funktionen om det inte tal är en int!!")


# testar = my_function()

if __name__ == '__main__':
    # testing my_function
    print('Testing my_function')
    my_function()