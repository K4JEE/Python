a = int(input('write first num: '))
b = int(input('write second num: '))
if a > b:
    for i in range(b, a+1):
        print(i)
else:
    for i in range(a, b+1):
        print(i)