print("Lutfen denklemin baskatsayilarini giriniz:\n")

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta=b**2 - 4*a*c

x1=(-b - delta**0.5) / (2*a)
x2=(-b + delta**0.5) / (2*a)

print("Denklemin birinci koku {}\nDenklemin ikinci koku{}".format(x1,x2))

# Bu kod da digeri gibi jupiter de çalıştı burda dosya cant find dedi ve çalıstırmadı amk
