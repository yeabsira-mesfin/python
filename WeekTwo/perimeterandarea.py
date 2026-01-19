continue_calculation = 'y'
while continue_calculation.lower().strip() == 'y':
    a = float(input(("Enter one side of the triangle:")))
    b = float(input(("Enter the other side of the triangle:")))
    c = float(input(("Enter the third side of the triangle:")))
    perimeter = a + b + c
    print(f"The perimeter of the triangle is: {perimeter}")
    area_question = input("Do you want to calculate the area of the triangle? (y/n):")
    if area_question.lower().strip() == 'y':
        d = float(input(("Enter the height of the triangle:")))
        e = float(input(("Enter the base of the triangle:")))
        area = (d * e / 2)
        print(f"The area of the triangle is: {area}")
    continue_calculation = input("Do you want to continue? (y/n):")