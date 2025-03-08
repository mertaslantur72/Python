import random
import time

class Araba:
    def __init__(self, isim):
        self.isim = isim
        self.hiz = 0

    def hizlan(self):
        hiz_artisi = random.randint(1, 6)
        self.hiz += hiz_artisi

    def yavasla(self):
        hiz_azaltma = random.randint(1, 3)
        self.hiz -= hiz_azaltma
        if self.hiz < 0:
            self.hiz = 0

    def durum(self):
        return f"{self.isim} arabası {self.hiz} birim hızında ilerliyor."


def yaris():
    arabalar = [
        Araba("Araba 1"),
        Araba("Araba 2"),
        Araba("Araba 3"),
        Araba("Araba 4")
    ]

    bitis_cizgasi = 100

    while True:
        for araba in arabalar:
            araba.hizlan()
            print(araba.durum())

            if araba.hiz >= bitis_cizgasi:
                print(f"{araba.isim} araba kazandı!")
                return

        print("-" * 20)
        time.sleep(1)


yaris()











