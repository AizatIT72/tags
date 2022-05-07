import random
import os
import pyfiglet
import time
from progress.bar import IncrementalBar
print(pyfiglet.figlet_format("TAG GAME"))
print('Добро пожаловать в игру пятнашки')
print('Правила: соберите все костяшки в порядке возрастания')
input('Нажмите Enter...')

mylist = [10, 22, 35, 44, 60, 69, 78, 100]
bar = IncrementalBar('Загрузка: ', max=len(mylist))

for item in mylist:
    bar.next()
    time.sleep(random.uniform(0, 0.3))
bar.finish()

if os.name == 'nt':
    os.system('cls')
else:
    print('Консоль не очищена')
number_list = [i for i in range(1, 16)]
number_list.append(' ')
result_list = list(zip(*[iter(number_list)] * 4))
for i in range(len(result_list)):
    result_list[i] = list(result_list[i])
random.shuffle(number_list)
area = list(zip(*[iter(number_list)] * 4))
for i in range(len(area)):
    area[i] = list(area[i])

col_width = max(len(str(num)) for row in area for num in row) + 2
while result_list != area:
    os.system('cls')
    for row in area:
        print(''.join(str(num).ljust(col_width) for num in row))
    row1 = int(input('Введите строку, откуда вы хотите переместить элемент: ')) - 1
    coluwn1 = int(input('Введите столбец, откуда вы хотите переместить элемент: ')) - 1
    row2 = int(input('Введите строку, куда вы хотите переместить элемент: ')) - 1
    coluwn2 = int(input('Введите столбец, куда вы хотите переместить элемент: ')) - 1
    if area[row2][coluwn2] == ' ' and abs(row2 - row1) == 0 and abs(coluwn2 - coluwn1) == 1 or abs(row2 - row1) == 1 and abs(coluwn2 - coluwn1) == 0:
        area[row1][coluwn1], area[row2][coluwn2] = area[row2][coluwn2], area[row1][coluwn1]
    else:
        print('Ячейка занята')
        continue
print('Поздравляю, вы победили')