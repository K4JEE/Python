lst = [1,4,6,7]
sum = []
for i in range(len(lst)):
    sum.append((lst[(i-1) % len(lst)]) + lst[(i+1) % len(lst)])

print(sum) 