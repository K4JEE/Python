from math import pow


numb = int(input('Write your number: '))
while numb > 0:
    print(int(pow(numb,3)))
    numb -= 1
