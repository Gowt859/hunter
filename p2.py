n1 = int(input())
L1 = list(map(int,input().split()))
L2 = sorted(L1)
k1 = len(L1)
#print(L,L2,k)
sum1 = L2[0]
a = 10
for i in range(1,len(L2)) :
    sum1 = sum1 + L2[i]*a
    a = a*10
print(sum1)
