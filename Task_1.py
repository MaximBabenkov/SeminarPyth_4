# Считать строку из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

import pathlib
from pathlib import Path
path = Path(pathlib.Path.cwd(), 'file1.txt') 

with open(path, 'r') as f:
    my_str = f.readline()
    print(my_str)  

numbs = my_str.split(" ")
digits = []
for elem in numbs:
    digits.append(int(elem))
 
print('The maximal number:', max(digits))
print('The minimal number:', min(digits))

    
