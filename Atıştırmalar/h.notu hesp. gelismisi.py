def gecenleri_bulma(su):
    su = su[:-1]
    dizim = su.split(',')

    ad = dizim[0]
    not1 = int(dizim[1])
    not2 = int(dizim[2])
    not3 = int(dizim[3])
    nihai_notlari = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)

    if (nihai_notlari >= 90):
        harf = "AA"
        return ad + '-------->' + harf + '\n'

    elif (nihai_notlari >= 85):
        harf = "BA"
        return ad + '-------->' + harf + '\n'

    elif (nihai_notlari >= 80):
        harf = "BB"
        return ad + '-------->' + harf + '\n'

    elif (nihai_notlari >= 75):
        harf = "CB"
        return ad + '-------->' + harf + '\n'

    elif (nihai_notlari >= 70):
        harf = "CC"
        return ad + '-------->' + harf + '\n'

    elif (nihai_notlari >= 65):
        harf = "DC"
        return ad + '-------->' + harf + '\n'

    else:
        return 'crınge'




def kalanlari_bulma(bardak):

    bardak = bardak[:-1]
    dizim = bardak.split(',')

    ad = dizim[0]
    not1 = int(dizim[1])
    not2 = int(dizim[2])
    not3 = int(dizim[3])
    nihai_notlari = not1 * (3 / 10) + not2 * (3 / 10) + not3 * (4 / 10)

    if (nihai_notlari >= 60 and nihai_notlari < 65):
        harf = "DD"
        return ad + '-------->' + harf + '\n'

    elif (nihai_notlari >= 55 and nihai_notlari < 60):
        harf = "FD"
        return ad + '-------->' + harf + '\n'

    elif(nihai_notlari < 55):
        harf = "FF"
        return ad + '-------->' + harf + '\n'

    else:
        return 'bos'




with open('notlar.txt','r',encoding='utf-8') as file:

    kalanlarin_listesi = list()
    gecenlerin_listesi = list()

    for i in file:

        if(kalanlari_bulma(i) == 'bos'):

            continue

        else:
            kalanlarin_listesi.append(kalanlari_bulma(i))

    file.seek(0) # Senin ben amk o.ç. İlk for da imleç sonda kaldığı için imleci basa almamız lazımmıs aw.

    for j in file:

        if(gecenleri_bulma(j) == 'crınge'):

            continue

        else:
            gecenlerin_listesi.append(gecenleri_bulma(j))



with open('gecenler.txt','w',encoding='utf-8') as file2:

    for k in gecenlerin_listesi:
        file2.write(k)



with open('kalanlar.txt','w',encoding='utf-8') as file3:

    for p in kalanlarin_listesi:
        file3.write(p)

print(gecenlerin_listesi)
print(kalanlarin_listesi)

