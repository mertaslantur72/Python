import math
import random
import time

print("""************

Sayı tahmin oyunu 

1 ile 50 arasındaki sayıyı tahmin edelim!

*************""")

rasgele_sayi=random.randint(1,50)
tahmin_hakki=7

while True:
    tahmin=int(input("Tahmininiz:"))

    if(tahmin<rasgele_sayi):
        print("Bilgiler kontrol ediliyor...")
        time.sleep(1)

        print("Daha büyük bir sayi soyleyiniz")
        tahmin_hakki-=1

    elif(tahmin>rasgele_sayi):

        print("Bilgiler kontrol ediliyor...")
        time.sleep(1)

        print("Daha kucuk bir sayi soyleyiniz")
        tahmin_hakki-=1

    else:

        print("Bilgiler kontrol ediliyor...")
        time.sleep(1)

        print("Tebrikler!!! Sayiyi dogru tahmin ettiniz...")
        break

    if(tahmin_hakki==0):

        print("Tahmin hakkiniz bitti. Sayiniz {} idi".format(rasgele_sayi))
        break
