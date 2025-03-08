a=list(range(1,101))
b=list(range(1,101))
c=list(range(1,101))

for i in range(0,100):

    for j in range(0,100):

        for k in range(0,100):

            if((a[k]**2 + b[j]**2)==c[i]**2):

                print("{}-{}-{} üçgeni".format(a[k],b[j],c[i]))