import sqlite3


con = sqlite3.connect("Magazanin_deposu.db")
cursor = con.cursor()

con.execute("CREATE TABLE IF NOT EXISTS mallarin_listesi(isim TEXT, turu TEXT, gramaj INT, fiyat INT)")
con.commit()


def urun_ekleme(isim,turu,gramaj,fiyat):
    con.execute("INSERT INTO mallarin_listesi VALUES(?,?,?,?)",(isim,turu,gramaj,fiyat))
    con.commit()

def depoyu_goster():

    cursor.execute("SELECT * FROM mallarin_listesi")
    data = cursor.fetchall()

    for i in data:
        print(i)


while True:

    islem = str(input("Hangi islemi yaparsınız?"))

    if(islem == "q"):
        break

    elif(islem == "1"):

        print("Ürün ekelmeye hos geldiniz...")
        a = str(input("Ürünün adı:"))
        b = str(input("Ürünün türü:"))
        c = int(input("Ürünün gramajı"))
        d = int(input("Ürünün fiyatı"))

        urun_ekleme(a, b, c, d)
        print("Ürüünüz eklendi sq")

    elif(islem == "2"):
        depoyu_goster()

con.close()