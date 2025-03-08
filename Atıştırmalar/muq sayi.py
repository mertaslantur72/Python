x = int(input('Test etmek istediğin sayıyı gir:'))
toplam=0

bolenler = list()
gavatlar = range(1,x)

for i in gavatlar:
    if(x % i == 0):
        bolenler.append(i)

for j in bolenler:
    toplam+=j

if(toplam==x):
    print('Bu sayi bir muq sayidir')

else:
    print('Bu siradan bir sayidir.')

