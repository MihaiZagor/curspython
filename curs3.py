# Cursul 3
import builtins
import random

choices = [x for x in range(11)]
print(choices)
while True:
    random_choice = random.choice(choices)
    if random_choice % 3 == 0:
        break
    print(f'random_choice:{random_choice}')

print(f'Last random_choice:{random_choice}')

def my_sum(a, b):
    return a + b
print(my_sum(1,2))

def my_function(list_param):
    list_param = list_param[::]
    list_param.append(99)
    print(f'list_param inner function {list_param}')
    #orice functie care nu are return are return none

my_list = [1, 2, 3]
my_function(my_list)
print(my_list)

def my_sum(*args):
    acc = 0
    for arg in args:
        acc += arg
    return acc

print(f'Suma totala {my_sum(1, 2, 3, 4, 5, 6)}')

my_var = input('Introduceti un nr:')
try:
    my_int = int(my_var)
    print(my_int)
except ValueError as e:
    print('Introduceti un numar intreg valid!')
except NameError as e:
    print('Pentru developer, ai grija la cod')
else:
    print('Ajungem aici daca nu avem exceptii!')
finally:
    print('Ajungem aici cu sau fara exceptii!')

print(dir(builtins))

def my_function():
    def my_second_function():
        # msg = 'coco'
        print(f'My second function here: {msg}')

    msg = 'Hello, World!'
    my_second_function()
    print(f'My function {msg}')

my_function()


