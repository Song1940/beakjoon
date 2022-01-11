a = input()
b = a.split('-')
answer =0

for i in b[0].split('+'):
    answer+=int(i)
for i in range(1,len(b)):
    for j in b[i].split('+'):
        answer -= int(j)

print(answer)
