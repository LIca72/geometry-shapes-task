import sys
import math

def square(parts):
    side = float(parts[5])
    perimeter = 4 * side
    area = side * side 
    return "Square", perimeter, area

def rectangle(parts):
    x1 = float(parts[2])
    y1 = float(parts[3])
    x2 = float(parts[5])
    y2 = float(parts[6])

    widht = abs(x1 - x2)
    height = abs(y1- y2)

    perimeter = 2 * (widht + height)
    area = widht * height
    return "Rectangle", perimeter, area

def circle(parts):
    radius = float(parts[5])
    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius
    return "Circle", perimeter, area

SHAPES = {
    "square": square,
    "rectangle": rectangle,
    "circle": circle
}
if __name__ == "__main__":
   
   for line in sys.stdin:
      
      line = line.strip()

      if not line:

        continue
      
      parts = line.split()
      shape_type = parts[0].lower()

      if shape_type in SHAPES:
           
           name, perimeter, area = SHAPES[shape_type](parts)
           print(f"{name} Perimeter{perimeter} Area{area}")