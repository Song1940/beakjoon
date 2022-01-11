n = input()
n = sorted(n, reverse=True)

a=' '

sum=0
for i in n:
    sum += int(i)

if '0' not in n or sum %3 != 0:
    print(-1)
else:
    print("".join(n))


