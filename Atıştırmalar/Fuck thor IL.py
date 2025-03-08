x=int(input('Lutfen  faktöriyelini istediğiniz sayiyi giriniz:'))
toplam=1

toplum = range(1,x+1)


for i in toplum:
    toplam=toplam*i

print('Girdiğiniz sayının faktöriyeli {} dir'.format(toplam))