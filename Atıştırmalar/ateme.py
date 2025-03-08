print('SoygunBannk a  Hossgeldiniz')
bakiye=1000
sifre=2549
girishakki=3


while True:

    password=int(input('Lutfen sifrenizi giriniz:'))

    if(password==sifre):

        x=int(input('Lütfen yapmak istediğiniz islemi seciniz:'))

        if(x==1):
            print('Bakiyeniz {} TL dir'.format(bakiye))
            break

        elif(x==2):
            gidici=int(input('Cekmek istediğiniz tutari giriniz:'))
            if(bakiye<gidici):
                print('O kadar paran yok')
                break

            else:
                print('Güle güle harcayiniz')
                bakiye = bakiye - gidici
                print('Kalan paraniz.{} tl dir'.format(bakiye))
                break

        elif (x == 3):
            gelir = int(input('Yatirmak istediğiniz tutari giriniz:'))
            print('Yeni paranız {} Tl olmustur.'.format(bakiye+gelir))
            break


        elif(x==4):
            cevap=str(input('Çıkmak istediğine eminsen?'))

            if(cevap=='evet'):
                break

            elif(cevap=='hayir'):
                continue

            else:
                print('SG evine aq senle ugrasamam')
                break

    else:
        print('Hatali sifre')
        girishakki-=1

        if(girishakki==0):
            print('sifre hakkin bitti')
            break

        else:
            continue