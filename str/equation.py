equation = 'y = -12x + 5'
x = 2.5
variable = equation.split(' ')
first = str(variable[2])
variable[2] = first[:-1]
y = float(variable[2]) * x + float(variable[4])
print(y)
