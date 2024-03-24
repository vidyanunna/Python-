a=input().split()
vow="aeiouAEIOU"
count=0
s=[]
for items in a:
    for char in items:
        if char in vow :
            count+=1
            s.append(char)
print(count)
