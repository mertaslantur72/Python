print("********************\nATM sistemine hoşgeldiniz\n********************")

print("""
İşlemler:
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan 'q' tuşu ile çıkabilirsiniz.
""")

bakiye=350

while True:

    islem=input("Islemi giriniz:")

    if (islem=="q"):
        print("Gule gule, yine bekeleriz...")
        break

    elif islem=="1":

        print("Bakiyenizde {} Tl vardir.".format(bakiye))
        continue

    elif islem=="2":
        para=int(input("Yatirmak istediginiz tutari giriniz:"))
        para+=bakiye
        print("Yeni bakiyeniz {} TL dir".format(para))
        bakiye=para
        continue

    elif islem=="3":
        gitti=int(input("Cekmek istediginiz tutari giriniz:"))

        if gitti>bakiye:
            print("Hesabinizda bu kadar para yoktur!!!")
            continue

        bakiye-=gitti

        print("Hesabinizda kalan para {} TL dir".format(bakiye))

        continue

    else:
        print("Lutfen adam gibi bir islem yapmaya calisiniz!!!!")