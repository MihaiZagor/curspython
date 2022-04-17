class Telefon:

    counter = 0

    def __init__(self, numar):
        self.numar = numar
        Telefon.counter += 1

    def apelare(self, numar_apelat):
        mesaj = f'Apelati {numar_apelat} folosind propiul numar'
        return mesaj

class TelefonFix(Telefon):

    last_SN = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonFix.last_SN += 1
        self.SN = f'TF - {TelefonFix.last_SN}'

class TelefonMobil(Telefon):

    last_SN = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonMobil.last_SN += 1
        self.SN = f'TM - {TelefonFix.last_SN}'


print('Numarul total de device-uri create', Telefon.counter)
t1 = TelefonFix('0742 883 478')
t2 = TelefonFix('0742 993 478')

t3 = TelefonMobil('0742 153 472')
t4 = TelefonMobil('0742 443 472')
print(t4.SN)

print('Numarul total de device-uri create', Telefon.counter)
