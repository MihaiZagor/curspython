from my_package.my_module import *
from my_package.my_second_module import *

# my_var = 6 o sa printeze 6, ca e variabila locala, ordinea e local, enclosed, global
if __name__ == '__main__':
    print('OK')
    print(my_var)
    print(my_func())