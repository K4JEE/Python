lst = [1,0,0,0,0,0,0,0,0,34,0,30,0,0,4,0,5,0,2]
for i in reversed(range(len(lst))):
    if lst[i] == 0:
        lst.append(lst.pop(i))
print(lst)