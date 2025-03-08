print("Faktoriyel hesaplayiciya hosgeldiniz...\n")

sayi=int(input("Lutfen faktoriyelini istediginiz sayiyi giriniz:"))
faktoriyel=1

if sayi<0:

    print("Negatif sayilarin faktoriyeli yoktur!")

else:

    for i in range(1,sayi+1):

        faktoriyel *= i

    print("{}'nin faktoriyeli {} dir.".format(sayi,faktoriyel))