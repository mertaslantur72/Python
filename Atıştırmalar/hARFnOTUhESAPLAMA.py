def not_hesaplama(satir):

    satir = satir[:-1]
    dizi = satir.split(',')
    print(dizi)

    isim = dizi[0]
    not1 = int(dizi[1])
    not2 = int(dizi[2])
    not3 = int(dizi[3])
    nihai_not =  not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (nihai_not >= 90):

        harf = "AA"
    elif (nihai_not >= 85):
        harf = "BA"
    elif (nihai_not >= 80):
        harf = "BB"
    elif (nihai_not >= 75):
        harf = "CB"
    elif (nihai_not >= 70):
        harf = "CC"
    elif (nihai_not >= 65):
        harf = "DC"
    elif (nihai_not >= 60):
        harf = "DD"
    elif (nihai_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + '-------->'+ harf + '\n'



with open('notlar.txt','r',encoding='UTF-8') as file:

    ekleneceklerin_listesi=list()

    for i in file:

        ekleneceklerin_listesi.append(not_hesaplama(i))

    with open('sonuclar.txt','w',encoding='UTF-8') as dosya:

        for j in ekleneceklerin_listesi:
            dosya.write(j)

print(ekleneceklerin_listesi[0]) # Demekki retur ettiğimiz şey tek bir string haline dönüşüyor

# Kurcalarken buluverdim :D CTRL + F yapıp X değişkenini aratıyorsun, ardından ALT tuşuna basarken ENTER'a basıyorsun bir kere hepsi seçili hale geliyor :)
"""
i file ın içinde dolaşırken satır satır geziyor, yani i nin ilk değeri "Hatice Günday,70,90,20" dir. Bunu da fonksiyona
verince (ki bu bir string dir) fonksiyon sonundaki \n i atıyor ardından ',' e göre parçalıyor bu tek parça olan 
string ifadeyi ve bu parçalar ile 'dizi' adında bir liste oluşturuyor. Bu diziden uygun bir şekilde isimi ve notları
alıp return olarak bir string ifade veriyor bunlar ile. Bu tek parça string de şöyle çıkıyor --> Hatice Günday-------->FD.
Fonksiyon ile işimiz bitti ve şimdi de 'notlar.txt' dosyasını okuyup bir for döngsü ile return den aldığımız tek parça
string ifadeleri 'ekleneceklerin_listesi' isimli listeye atıyoruz. Ardından 'sonuclar.txt' dosyasını yazıp yine bir
for döngüsü ile yazıyoruz.
"""