def triangle_type(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2] or min(sides) <= 0:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def main():
    print("Enter the lengths of the sides of a triangle to see what type it is!")
    try:
        a = float(input("Enter side 1: "))
        b = float(input("Enter side 2: "))
        c = float(input("Enter side 3: "))
        print("Triangle type:", triangle_type(a, b, c))
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()