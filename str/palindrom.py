str = input('Write your text: ')
str = str.replace(' ','')
new_str = str[::-1]
if str == new_str:
    print('Palindrom')
else:
    print('No palindrom')