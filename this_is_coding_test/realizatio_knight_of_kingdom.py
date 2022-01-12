position = input()
column = ord(position[0])-ord('a')+1
row = int(position[1])


knight_moves = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]

cnt=0

for i in range(len(knight_moves)):
    ncolumn = column +knight_moves[i][0]
    nrow = row + knight_moves[i][1]
    if ncolumn <1 or ncolumn>8 or nrow<1 or nrow>8:
        continue
    cnt+=1
print(cnt)