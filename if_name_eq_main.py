from fun_imports import my_function, print_sträng_tal_number_of_times
# from fun_imports import *
# my_dict = {1:2}

def print_dict(d):
    print(d)

def main():
    my_dict = {1:2}

    print('Kör main function!')
    print(print_dict(my_dict))
    # my_function()
    # print(glob_dict) 

if __name__ == '__main__':
    main()
else:
    print('Vi kör inte main-function!!!')