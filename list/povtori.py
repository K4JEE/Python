n = [1,1,2,2,2,4,5,6,7]
lst = 0
for i in n:
    lst += n.count(i)-1
    n.remove(i)
print(lst)
