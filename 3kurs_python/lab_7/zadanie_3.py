import random
import math

for _ in range(10):
    num = random.randint(-10, 10)
    
    if num < 0:
        continue
    elif num == 0:
        break
    
    sqrt_num = math.sqrt(num)
    print(f"Квадратный корень числа {num}: {sqrt_num}")
    input()
