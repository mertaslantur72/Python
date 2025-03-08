print("Amstrong Sayi Uygulamasina Hosgeldiniz...")

p=k=sayi=int(input("Lutfen sayiyi giriniz:"))
toplam=0
sayac=0
i=0

while(sayi!=0):

   if(sayi%10==0):
      sayi=(sayi/10)
      sayac+=1

   else:
      sayi=(sayi-(sayi%10))/10
      sayac+=1

print("Girdiginiz sayi {} basamaklidir".format(sayac))

while(i<sayac):
   if(p%10==0):
      toplam+=1
      p=p/10
      i+=1

   else:
      toplam+=((p%10)**sayac)
      p=((p-(p%10))/10)
      i+=1

if(toplam==k):
   print("Girdiginiz sayi bir Amstrong sayidir.")

else:
   print("Bu sayi Amstrong sayi degildir.")



#Burada bir sayinin kaç basamakli oldugunu ogrendin. not:1634 bir amstrong sayidir.
"""
Ayrıca girilen sayinin basamak sayisini bulmak için aşagıdakş kodu da kullanabildirdin

!!!!!!!!!!!
sayi=(input("Lutfen sayi giriniz:"))

print(len(sayi))
!!!!!!!!!!!!!!!

ama burada da int(input()) yapma, öyle kabuletmiyor!!!

"""