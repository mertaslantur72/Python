print("You're welcome to calculating car.")

yakıt=float(input("Kac litre yakıyor:"))
yol=int(input("Kac km gidecen:"))
fiyat=float(input("Mazot gac para:"))

masraf=float( ((yakıt*fiyat)/100)*yol )

print("Gideceginiz yol masrafı {:.3f} TL dir".format(masraf))
print("Iyi yolculuklar dileriz")

#girdi degerlerinde inputun içine şunu şunu lutfen giriniz gibi bir ifade yazarsam float da hata veriyor lakin
#sadece input() yazarsam hata vermeden float ilşe işlem yapabiliyorum. Why?? Not: Düzelttim:))