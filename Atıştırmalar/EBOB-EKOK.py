def ebob_ekok(sayi1, sayi2):
    bolenleri1 = []
    bolenleri2 = []

    for i in range(1, sayi1 + 1):
        if sayi1 % i == 0:
            bolenleri1.append(i)

    for j in range(1, sayi2 + 1):
        if sayi2 % j == 0:
            bolenleri2.append(j)

    bolenleri1.sort(reverse=True)
    bolenleri2.sort(reverse=True)

    for k in bolenleri1:
        for p in bolenleri2:
            if k == p:
                obeb = p
                okek = (sayi1 * sayi2) // obeb
                return obeb, okek

    return None, None


sayi1 = int(input('Lütfen ilk sayıyı giriniz: '))
sayi2 = int(input('Lütfen ikinci sayıyı giriniz: '))

ebob, ekok = ebob_ekok(sayi1, sayi2)

print('EBOB: ', ebob)
print('EKOK: ', ekok)
