li1 = [1,2,4,5,9,8]
k=6


li= ["banana","apple","banana","mango","mango","mango"]
li2 = []
for i in li:
    if i not in li2:
        li2.append(i)
print(li2)
for i  in li2:
    count = 0
    if i in li:
        count +=1
print("{} {} times".format(i,count))
    