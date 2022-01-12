n = int(input())

plans = input().split()

x,y =1,1

moves = ['U','D','L','R']
dx = [-1,1,0,0]
dy = [0,0,-1,1]


for plan in plans:
    for i in range(len(moves)):
        if plan == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    x,y = nx,ny

print(x,y)