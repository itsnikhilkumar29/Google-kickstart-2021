def f(x,y):
    x=ord(x)
    y=ord(y)
    return min(abs(x-y),26-abs(x-y))

for _ in range(int(input())):
    s=input()
    t=input()
    count=0
    for i in s:
        m=100
        for j in t:
            m=min(m,f(i,j))
        count+=m
    print(f'Case #{_+1}: {count}')
