lst = input('Write your text: ')
lst = lst.replace(' ','')
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(''.join(new_lst))