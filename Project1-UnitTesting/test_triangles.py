from triangles import triangle_type

def test_scalene():
    assert triangle_type(3, 4, 5) == "Scalene"
    assert triangle_type(5, 4, 3) == "Scalene"
    assert triangle_type(999.999, 1020, 1999) == "Scalene"

def test_isosceles():
    assert triangle_type(5, 5, 1) == "Isosceles"

def test_equilateral():
    assert triangle_type(1, 1, 1) == "Equilateral"

def test_not_a_triangle():
    assert triangle_type(1, 2, 3) == "Not a triangle"
    assert triangle_type(0, 1, 1) == "Not a triangle"
    assert triangle_type(-1, 2, 3) == "Not a triangle"
    assert triangle_type(1, 2, 10) == "Not a triangle"