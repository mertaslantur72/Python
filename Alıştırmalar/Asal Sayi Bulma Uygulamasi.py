def asal_mi(sayi):
    sayac=0

    if(sayi<=0):
        print("Bu sayi asal degildir")

    else:

        for i in range(1,sayi+1):

            if(sayi%i==0):
                sayac+=1

        if(sayac==2):
            print("Bu sayi asaldir")
        else:
            print("Bu sayi asal degildir")

print(asal_mi(2))