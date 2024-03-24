#[1,2,1,2,3,1,4]=[1,2,3,4]
numbers = input().split()
numbers = [int(item) for item in numbers]
unique_num = []

for item in numbers:
    if item not in unique_num:
        unique_num.append(item)

print("Unique numbers:", unique_num)
