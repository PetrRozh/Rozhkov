a = [i+1 for i in range(50)]
a.sort(reverse=True)
for i in range(len(a)):
    el1=a[i]
    el2=a[i+1]
    el3=a[i+2]
    if el1+el2>el3 and el2+el3>el1 and el1+el3>el2:
        p=(el1+el2+el3)//2
        s=(p*(p-el1)*(p-el2)*(p-el3))**0.5
        break
print(s,el1,el2,el3)
