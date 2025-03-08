import random
import time

rastgele_sayi = random.randint(1,100)
tahmin_hakki=5

while True:

    sayi = int(input('Lutfen sayiyi giriniz:'))

    if(sayi<rastgele_sayi):

        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print('Lutfen daha buyuk sayi giriniz')
        tahmin_hakki-=1

    elif(sayi>rastgele_sayi):

        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)

        print('Lutfen daha kucuk bir sayi giriniz')
        tahmin_hakki-=1

    else:
        print('Dogru tahmin ettiniz')
        break


    if(tahmin_hakki==0):
        print('Hakkınız bitti. Dogru sayi {} idi'.format(sayi))
        break

        # Not: bu kod ufak tefek salaklıklar içerir fakat bunlar önemli değildir.