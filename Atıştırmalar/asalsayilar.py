print('Asallik belirleyicisine hoşgeldiniz...')
bolenleri=list()
sayi=int

def asal_bulucu(sayi):
    while True:

        sayi = int(input('Lütfen test etmek istediğiniz sayıyı giriniz:'))


        for i in range(1, sayi + 1):

            if (sayi % i == 0):
                bolenleri.append(i)

        if (len(bolenleri) == 2):
            print('Asaldir.')

        else:
            print('Asal değildir\nBölenleri şunlardır--->{}'.format(bolenleri))

        bolenleri.clear()

asal_bulucu(sayi)

