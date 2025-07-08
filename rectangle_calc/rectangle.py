import calculate

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area_result = calculate.area(length, width)
perimeter_result = calculate.perimeter(length, width)

print(f"The area of the rectangle is: {area_result}")
print(f"The perimeter of the rectangle is: {perimeter_result}")
