lst = input('Write your text please: ')
count_small = 0
count_big = 0
for i in lst:
    if 'a' <= i <= 'z':
        count_small += 1
    elif 'A' <= i <= 'Z':
        count_big += 1

print(f'Small word: {count_small}')
print(f'Big word: {count_big}')