prime = [False]+[False]+[True]*10000

for i in range(2,101):
    if prime[i] == True:
        for j in range(i+i,10001,i):
            prime[j] = False

answer_list =[]

n = int(input())
for i in range(n):
    m = int(input())
    a = m//2
    b = a
    for j in range(m):
        if prime[a] and prime[b]:
            answer_list.append([a,b])
            break
        else:
            a-=1
            b+=1
for i in answer_list:
    print(i[0],i[1])


