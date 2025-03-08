def okunus(sayi):

    birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
    onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

    bir=sayi%10
    on=sayi//10

    print(onlar[on],birler[bir])

sayi=int(input("Lutfen bir sayi giriniz:"))
okunus(sayi)