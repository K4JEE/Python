lst = [1,3,4,5,5,6,6,8,8,7,7,7,8,9]
new_lst = []
for i in lst:
    if lst.count(i) >= 2:
        new_lst.append(i)
finally_lst = []
for i in new_lst:
    if i in finally_lst:
        pass
    else:
        finally_lst.append(i)
print(finally_lst)