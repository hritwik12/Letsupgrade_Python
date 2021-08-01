#program 1 delete occurence
n=list(map(int,input().split()))
d=[]
for i in n:
    if i not in d:
        d.append(int(i))
print(d)
