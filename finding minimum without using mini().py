number=map(int,input().split())
mini=999
for num in number:
    while num<mini:
        mini=num
print(mini)
