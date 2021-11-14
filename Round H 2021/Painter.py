#store compositions of every secondary color in a dictionary
sec_to_pri={'O':{'R','Y'},'P':{'R','B'},'G':{'B','Y'},'A':{'R','Y','B'},'U':{}}

#this function finds the number of strokes (contiunous blocks) of given color in the array
def f(s,x):
    c=0
    l=0
    for i in s:
        if i==x or (i in sec_to_pri and x in sec_to_pri[i]):
            l+=1
        else:
            if l>0:
                c+=1
                l=0
        # print(l,end='')
    # print()
    if l>0:c+=1
    return c
for _ in range(int(input())):
    n=int(input())
    s=input()
    count=f(s,'R')+f(s,'B')+f(s,'Y')
    print(f'Case #{_+1}: {count}')
