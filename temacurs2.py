# declarare lista
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print('Lista initiala:', my_list)

# ordonare lista ascendent
my_list.sort()
# afisare lista ordonata descendent
print('Lista ordonata ascendent:', my_list)

# ordonare lista descendent
my_list.sort(reverse=True)
# afisare lista ordonata descendent
print('Lista ordonata descendent:', my_list)

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# numerele pare din lista
my_list_even = my_list[::2]
# afisarea numerelor pare din lista
print('Numerele pare din lista', my_list_even)

# numerele impare din lista
my_list_odd = my_list[1::2]
#afisarea numerelor impare din lista
print('Numere impare din lista', my_list_odd)

# elementele multiple lui 3 din lista
multiple_three = []
for i in my_list:
    if i % 3 == 0:
        multiple_three.append(i)
# afisare elemente
print(multiple_three)


