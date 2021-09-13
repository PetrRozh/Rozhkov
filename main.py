n=int(input('Введи кол-во чисел: '))
a=[]
for i in range(n):
    a += list(map(int, input().split()))
a.sort(reverse=True)
f=0
for i in range(n):
    if a[i]<1:
        f=+1
        break
    else: continue
if f==0:
    for i in range(len(a)):
        el1=a[i]
        el2=a[i+1]
        el3=a[i+2]
        if el1+el2>el3 and el2+el3>el1 and el1+el3>el2:
            p=(el1+el2+el3)//2
            s=(p*(p-el1)*(p-el2)*(p-el3))**0.5
            break
    print(s,el1,el2,el3)
