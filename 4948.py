def isprime(m,n):
    n+=1
    cnt =0
    prime = [True]*n
    for i in range(2,int(n*0.5)+1):
        if prime[i] ==True:
            for j in range(i+i,n,i):
                prime[j]=False
    for i in range(m+1,n):
        if i>1 and prime[i]==True:
            cnt+=1

    return cnt

list = []

while 1:
    n = int(input())
    if n ==0:
        break
    list.append(isprime(n,n*2))

for i in list:
    print(i)
