import sys

n = int(sys.stdin.readline())
list = [[0]*2 for i in range(n)]


for i in range(n):
    a,b = map(int,(input().split()))
    list[i][0] = a
    list[i][1] = b

list.sort(key = lambda x:(x[1],x[0]))

cnt =1
end_time = list[0][1]
for i in range(1,n):
    if list[i][0]>=end_time:
      cnt +=1
      end_time = list[i][1]

print(cnt)