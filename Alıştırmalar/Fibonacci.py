a=1
b=1
fibonaci=[a,b]

for i in range(20):

    a,b=b,a+b

    fibonaci.append(b)

print(fibonaci)