def sum_simple(a):
    if a <= 0:
        return 0

    return a + sum_simple(a-1)

def sum_even(b):
    if b <= 0:
        return 0
    else:
        even = 0
    for i in range(b+1):
        if i % 2 == 0:
            even += i
        else:
            even = 0
    return even + sum_even(b-1)

def sum_odd(c):
    if c <= 0:
        return 0
    else:
        odd = 0
    for i in range(c+1):
        if i % 2 != 0:
            odd += i
        else:
            odd = 0
    return odd + sum_odd(c-1)