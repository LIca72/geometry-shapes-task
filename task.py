# Алгоритм програми
# 1. читаємо рядок
# 2. розбиваємо split()
# 3. визначаємо тип фігури
# 4. беремо параметри
# 5. рахуємо площу і периметр

import sys
import math

for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    shape_type = parts[0]

    if shape_type == "Square":
        side = float(parts[5])

        perimeter = 4 * side
        area = side * side

        print(f"Square Perimeter {perimeter} Area {area}")

    if shape_type == "Rectangle":
        x1 = float(parts[2])
        y1 = float(parts[3])
        x2 = float(parts[5])
        y2 = float(parts[6])

        width = abs(x1 - x2)
        heigth = abs(y1 - y2)

        perimeter = 2 * (width + heigth)
        area = width * heigth
        print(f"Rectangle Perimeter {perimeter} Area {area}")

    if shape_type == "Circle":
        radius = float(parts[5])
        perimeter = 2 * math.pi * radius
        area = math.pi * radius * radius
        print(f"Circle Perimeter {perimeter} Area {area}")

