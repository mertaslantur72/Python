toplum = [1, 1]
x = int(input('Kaç tane hesaplanmasını istersiniz:'))
for i in range(1,x):
    ygt = toplum[i] + toplum[i-1]
    toplum.append(ygt)

print(toplum)
