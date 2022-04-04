print('Hello World!')

for i in range(2):
    print(f"Hello World!{i}")

def new_function(a, b):

    return a + b

print(type(2))

l = []
n = []
if not l:
    print('lista vida')

print (l is n) # printeaza False deoarece ocupa adrese de memorie diferite (compara daca sunt aceleasi obiecte)
print (l == n) # printeaza True deoarece sunt egale

nume = 'Popescu'
prenume = 'Florin'

body_text = f""""
Buna ziua!

Ma numesc {nume} {prenume}

Bine ati venit pe site-ul nostru
"""  # f din fata ghilimelelor e pentru interpolare

print(body_text)

l = [1, 2, 3]
print(l)
l[1] = 0
print(l)

name ='Marius'
print(name[1])
# name[0] = 'D' eroare deoarece nu se poate schimba string-ul (nu se pot modifica, caracterele din interiorul lui)

l = [1, 2, 3, 5, 6, 7, 8, 9, 10]

g = l[:]
l[0] = 'a'
print(l)
print(g)