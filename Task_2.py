# Найдите корни квадратного уравнения AX^2 + BX + C = 0

import pathlib
from pathlib import Path
path = Path(pathlib.Path.cwd(), 'file2.txt') 

with open(path, 'r') as f:
    my_str = f.read()
numbs = my_str.split("\n")
digits = []
for elem in numbs:
    digits.append(int(elem))
print(digits)

d = digits[1]**2 - 4*(digits[0]*digits[2])
print(d)

x_1 = (-digits[1] + (d**0.5)) / (2 * digits[0])
x_2 = (-digits[1] - (d**0.5)) / (2 * digits[0])

print(round((x_1), 2))
print(round((x_2), 2))
