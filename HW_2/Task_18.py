# 18. Реализуйте алгоритм перемешивания списка.

import random
list = [random.randint(0,10) for i in range(random.randint(3,15))]
print(f"Первоначальный список:\n {list}")
random.shuffle(list)
print(f"Перемешанный список:\n{list}")