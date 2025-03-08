print('Bil bakalım kaç tane var a hos geldiniz...')

with open('metin.txt','r',encoding='utf-8') as file:
    metin = file.read()
    kelimeler = metin.split()
    temiz_kelimeler = list()
    file.seek(0)

    for i in kelimeler:

        i = i.strip('\n')
        i = i.strip(' ')
        i = i.strip('.')
        i = i.strip(',')

        temiz_kelimeler.append(i)

    kucultulmus_kelimeler = list()

    for j in temiz_kelimeler:
        kucultulmus_kelimeler.append(j.lower())

    summ =0

    a = str(input('Lütfen metininiz içerisinde aradığınız şeyi buraya yazınız:'))

    for k in kucultulmus_kelimeler:
        summ += int(k.count(a))

    print('Bu metin içerisinede {} ifadesinden toplamda {} tane vardır'.format(a,summ))







