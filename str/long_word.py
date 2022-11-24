str = input('Write your text: ')
new_str = str.split(' ')
print(max(new_str, key=len))