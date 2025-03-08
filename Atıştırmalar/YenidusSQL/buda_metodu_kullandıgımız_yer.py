from bu_metod_olacak import *

print("""**************
Depo yönetimi sayfasına hoşgeldiniz...

1.Depodaki tüm ürünleri gösterme
2.Depoda ürün koduna göre ürün sorgulama
3.Depoya ürün ekleme
4.Depodan ürün silme
5.Depodaki bir ürünün bilgilerini değiştirme

Çıkış yapmak için ise lütfen 'q' tuşuna basınız
******************""")

denek = Depo()

while True:
    islem = str(input("Lütfen yapmak istediğiniz işlemin numarasını giriniz:"))


    if(islem == "q"):
        print("Sistemden çıkılıyor, bekleyiniz...")
        time.sleep(3)
        print("Güle güle...")
        break

    elif(islem == "1"):
        print("Ürünler listeleniyor, lütfen bekleyiniz....")
        time.sleep(3)
        denek.urunleri_goruntuleme()


    elif (islem == "2"):
        p = str(input("lütfen sorgulamak istediğiniz ürünün kodunu giriniz:"))
        print("Ürün sorgulanıyor, lütfen bekleyiniz...")
        time.sleep(3)
        denek.urun_sorgulama(p)

    elif (islem == "3"):
        isim = str(input("Lütfen eklenecek ürünün adını giriniz:"))
        kategori = str(input("Lütfen eklenecek ürünün kategorisini giriniz:"))
        urun_kodu = str(input("Lütfen eklenecek ürünün kodunu giriniz:"))
        gramaj = int(input("Lütfen eklenecek ürünün gramajını giriniz:"))
        fiyat = int(input("Lütfen eklenecek ürünün fiyatını giriniz:"))

        print("Ürün sisteme ekleniyor, lütfen bekleyiniz...")
        time.sleep(3)

        kekstra = Urun(isim,kategori,urun_kodu,gramaj,fiyat)

        denek.urun_ekleme(kekstra)
        print("Ürün sisteme başarıyla kaydedilmiştir.")


    elif (islem == "4"):
        puf = str(input("Lütfen silmek istediğiniz ürününismini giriniz:"))
        print("Ürün sistemden siliniyor, lütfen bekleyiniz...")
        time.sleep(3)

        denek.urun_sil(puf)


    elif (islem == "5"):
        beypazari = str(input("Lütfen bilgilerini değiştirmek istediğiniz ürünün kodunu giriniz:"))

        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        time.sleep(3)

        denek.urun_bilgileri_degistir(beypazari)



