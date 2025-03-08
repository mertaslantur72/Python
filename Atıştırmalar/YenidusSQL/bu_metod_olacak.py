import sqlite3
import time
import sys

class Urun():

    def __init__(self,isim,kategori,urun_kodu,gramaj,fiyat):
        self.isim = isim
        self.kategori = kategori
        self.urun_kodu = urun_kodu
        self.gramaj = gramaj
        self.fiyat = fiyat

    def __str__(self):
        return "Ürünün İsmi:{}\nÜrünün Kategorisi:{}\nÜrünün Kodu:{}\nÜrünün Gramajı:{}\nÜrünün Fiyatı:{}\n".format(self.isim,self.kategori,self.urun_kodu,self.gramaj,self.fiyat)

class Depo():

    def __init__(self):
        self.db_olusturma()


    def db_olusturma(self):
        self.con = sqlite3.connect("Magazanin_deposu.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS deponun_tablosu(isim TEXT, kategori TEXT, urun_kodu TEXT, gramaj INT, fiyat INT)")
        self.con.commit()

    def db_baglanti_kesici(self):
        self.con.close()

    def urunleri_goruntuleme(self):

        self.cursor.execute("SELECT * FROM deponun_tablosu")
        data = self.cursor.fetchall()

        if(len(data) == 0):
            print("Depoda ürün bulunmamaktadır.")

        else:
            for i in data:
                print(i[0],i[1],i[2],i[3],i[4])

    def urun_sorgulama(self,urun_kodu):
        #Burada self in yanına x falan diyemezsim, sütün ismi ile aynı, yani urun_kodu olmak zorunda parametren
        self.cursor.execute("SELECT * FROM deponun_tablosu where urun_kodu = ?",(urun_kodu,))
        buldukum_urun = self.cursor.fetchall()

        if(len(buldukum_urun) == 0):
            print("Bu ürün depoda bulunamadı")

        else:
            kek = Urun(buldukum_urun[0][0],buldukum_urun[0][1],buldukum_urun[0][2],buldukum_urun[0][3],buldukum_urun[0][4])
            print(kek)


    def urun_ekleme(self,yeni_urun):

        self.cursor.execute("INSERT INTO deponun_tablosu VALUES(?,?,?,?,?)",(yeni_urun.isim,yeni_urun.kategori,yeni_urun.urun_kodu,yeni_urun.gramaj,yeni_urun.fiyat))
        self.con.commit()
        #EXECT daki en sondaki "yeni_urun.isim" ksımına takılma. Oradak isim yerine x de diyebilirsin. Onlar sadece ilerde
        #?---> yer tutucunun yerini alacak olan değerler olacak.

    def urun_sil(self,isim):

        self.cursor.execute("SELECT * FROM deponun_tablosu WHERE isim = ? ", (isim,))
        result = self.cursor.fetchall()

        if(len(result) == 0):
            print("Depoda bu isimde bir ürün yok.")
            return

        else:

            self.cursor.execute("DELETE FROM deponun_tablosu WHERE isim = ?", (isim,))
            self.con.commit()
            print("Ürün başarıyla sistemden silindi")




    def urun_bilgileri_degistir(self, urun_kodu):
        self.cursor.execute("SELECT * FROM deponun_tablosu where urun_kodu = ?", (urun_kodu,))
        bilgisi_degisecek_urun = self.cursor.fetchall()
        bilgisi_degisecek_urun = list(bilgisi_degisecek_urun)

        if len(bilgisi_degisecek_urun) == 0:
            print("Depoda bu ürün koduna ait mal bulunmamaktadır.")
            sys.exit()
        else:
            print(""" ****************
            ÜRÜN DEĞİŞTİRİCİ TABLOSU (OPSİYONLAR)
            1.İsim
            2.Kategori
            3.Ürün kodu
            4.Gramaj
            5.Fiyat
            Ana menüye dönmek için ise q tuşuna basınız
            *************\n""")

            while True:

                islem_tusu = str(input("Ürüne ait hangi bilgiyi değiştirmek istersiniz:"))

                if islem_tusu == "1":
                    yeni_isim = str(input("Lütfen ürünün yeni ismini giririniz:"))
                    self.cursor.execute("UPDATE deponun_tablosu SET isim = ? WHERE urun_kodu = ?",(yeni_isim, urun_kodu))

                    self.con.commit()
                    print("İşleminiz başarıyla gerçekleştirilmiştir.")

                elif islem_tusu == "q":
                    print("Programdan çıkılıyor...")
                    time.sleep(3)
                    break

                elif islem_tusu == "2":
                    yeni_kategori = str(input("Lütfen ürünün yeni kategorisini giririniz:"))
                    self.cursor.execute("UPDATE deponun_tablosu SET kategori = ? WHERE urun_kodu = ?",(yeni_kategori, urun_kodu))

                    self.con.commit()
                    print("İşleminiz başarıyla gerçekleştirilmiştir.")

                elif islem_tusu == "3":
                    print("Bir ürünün ürün kodunu değiştiremezsiniz!\nLütfen alt menünden başka bir işlem seçiniz")
                    continue

                elif islem_tusu == "4":
                    yeni_gramaj = int(input("Lütfen ürünün yeni gramajını giriniz:"))
                    self.cursor.execute("UPDATE deponun_tablosu SET gramaj = ? WHERE urun_kodu = ?",(yeni_gramaj, urun_kodu))

                    self.con.commit()
                    print("İşleminiz başarıyla gerçekleştirilmiştir.")

                elif islem_tusu == "5":
                    yeni_fiyat = int(input("Lütfen ürünün yeni fiyatini giriniz:"))
                    self.cursor.execute("UPDATE deponun_tablosu SET fiyat = ? WHERE urun_kodu = ?",(yeni_fiyat, urun_kodu))

                    self.con.commit()
                    print("İşleminiz başarıyla gerçekleştirilmiştir.")

                    """
                    self.cursor.execute("UPDATE deponun_tablosu SET isim = ? WHERE urun_kodu = ?", (yeni_isim, urun_kodu))
                    bunu kullan sql de bir şeyi update etmenin de fonku varmıs amk bosuna ugrasmıssın yarrımn yaparsın onu da.
                    """




