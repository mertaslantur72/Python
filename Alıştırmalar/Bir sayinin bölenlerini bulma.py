sayi=int(input("Lutfen sayiyi giriniz:"))
liste1=list()
sayac=0



for i in range(1,sayi+1):

    if(sayi%i==0):

        liste1.append(i)
        sayac+=1

print("{}'in {} tane böleni vardır.".format(sayi,sayac))
print(liste1)



