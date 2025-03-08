print("Mukemmel Sayi Uygulamasina Hosgeldiniz...")

x=int(input("Lutfen sayi giriniz:"))
i=1
toplam=0

while(i<x):
    if(x%i==0):
        toplam+=i
    i+=1

if(x==toplam):
    print("Sayiniz bir mukemmlel sayidir.")

else:
    print("Bu sayi mukemmel sayi degildir.")