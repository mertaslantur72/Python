def EBOB(sayi1,sayi2):

    sayac1=0
    sayac2=0

    liste1=list()
    liste2=list()

    for i in range(1, sayi1 + 1):

        if (sayi1 % i == 0):
            liste1.append(i)
            sayac1+=1

    for j in range(1,sayi2+1):

        if(sayi2%j==0):
            liste2.append(j)
            sayac2+=1


#Buraya kadar sayıların bölenlerini listeledik ve kaçar adet böleni olduklarını sakladık.

    if(sayac1>=sayac2):

       for p in range(1,sayac1+1):

           if(liste1[sayac1-p]==liste2[sayac2-p]):
               print("EBOB'unuz {} dir".format(liste1[sayac1-p]))

    else:

        for p in range(1, sayac2+1):

            if (liste1[sayac1 - p] == liste2[p-1]):
                print("EBOB'unuz {} dir".format(liste1[sayac1-1]))

EBOB(12,72)

#Malesef şuan bunu da yapamadın. Ama birinci "#" ye kadar her şeyi doğru yaptın.
#Eksik kalan yerin ise yaptığın iki listedeki en büyük ortak sayıyı bulmak. Onu da yaparsan tamamdır.