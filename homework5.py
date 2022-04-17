
class Fractie():

    def __init__(self, numarator, numitor):
        self.numarator = int(numarator)
        self.numitor = int(numitor)
        if self.numitor < 0:
            self.numitor = abs(self.numitor)
            self.numarator = -1*self.numarator
        elif self.numitor == 0:
            raise ZeroDivisionError

    def __str__(self):
        return (f'{self.numarator}/{self.numitor}')

    def __add__(self, other):
        return (f'{self.numarator*other.numitor + self.numitor*other.numarator}/{self.numitor*other.numitor}')

    def __sub__(self, other):
        return (f'{self.numarator * other.numitor - self.numitor * other.numarator}/{self.numitor * other.numitor}')

    def inverse(self):
        return (f'{self.numitor}/{self.numarator}')


f1 = Fractie(4, -5)
f2 = Fractie(3, 4)
f3 = Fractie.__add__(f1, f2)
f4 = Fractie.__sub__(f1, f2)
f5 = Fractie.inverse(f2)
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)
