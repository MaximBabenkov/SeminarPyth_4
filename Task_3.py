# Задайте два числа. Напишите программу, которая найдет НОК
# - наименьшее общее кратное этих двух чисел

def find_gcd(a: int, b: int):
    while a != 0 and b !=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    great_com_divis = a + b
    return great_com_divis

def find_lcm(a: int, b: int, gr_com_div: int):
    least_com_mult = (a * b) / gr_com_div
    return least_com_mult

import pathlib
from pathlib import Path
path = Path(pathlib.Path.cwd(), 'file3.txt') 

with open(path, 'r') as f:
    my_str = f.read()
numbs = my_str.split("\n")
digits = []
for elem in numbs:
    digits.append(int(elem))
print(digits)
 
a = digits[0]
b = digits[1]
gcd = find_gcd(a, b)
lcm = find_lcm(a, b, gcd)
print('Least common multiple:', int(lcm))