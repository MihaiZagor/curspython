#ex1.
def sum_param(*args):
    sum = 0
    for i in args:
        if isinstance(i, int):
            sum += i
        elif i == 0:
            sum = 0

    return print(sum)


sum_param('a', 1, 'b', 3, 'abs', 3)
sum_param()
# print(sum_param) intrebare: de ce aici nu imi returneaza valoarea sumei?

#ex2
def find_integer():
    valid = False
    while not valid:
        try:
            value = int(input('Please enter an integer else I will return 0:\n'))
            return value
            # print(f'Your integer is:{value})
            valid = True

        except ValueError:
            return 0
        break


# find_integer() intrebare: de ce asa nu functioneaza corect functia? (nu returneaza valoarea nr. intreg sau 0)
print(find_integer())

#ex3
import rec_functions
a = int(input('Give me an integer number, please:\n'))
print(f'Sum of numbers to {a}:{rec_functions.sum_simple(a)}')
print(f'Sum of even numbers to {a} :{rec_functions.sum_even(a)}')
print(f'Sum of odd numbers to {a}:{rec_functions.sum_odd(a)}')
