gift_presented_to=list(map(int,input().split()))
gift_recevied_from=[]
for i in range(1,len(gift_presented_to)+1):
    gift_recevied_from.append(gift_presented_to.index(i)+1)
print(gift_recevied_from)
