a = [1,2,3,4,5]

def push(e):
    global a
    a.append(e)

def pop():
    global a
    if len(a) != 0:
        return a.pop(-1)

pop()
print(a)
push(10)
print(a)