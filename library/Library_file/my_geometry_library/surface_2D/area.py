import math

# 1. Rectangle


def rectangle(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    - length (float): Length of the rectangle.
    - width (float): Width of the rectangle.

    Returns:
    float: Area of the rectangle.
    """
    return length * width

# 2. Square


def square(side):
    """
    Calculate the area of a square.

    Parameters:
    - side (float): Side length of the square.

    Returns:
    float: Area of the square.
    """
    return side ** 2

# 3. Circle


def circle(radius):
    """
    Calculate the area of a circle.

    Parameters:
    - radius (float): Radius of the circle.

    Returns:
    float: Area of the circle.
    """
    return math.pi * radius ** 2

# 4. Triangle


def triangle(side1, side2, side3):
    """
    Calculate the area of a triangle using Heron's formula.

    Parameters:
    - side1 (float): Length of the first side of the triangle.
    - side2 (float): Length of the second side of the triangle.
    - side3 (float): Length of the third side of the triangle.

    Returns:
    float: Area of the triangle.
    """
    # Calculate semi-perimeter
    s = (side1 + side2 + side3) / 2

    # Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

# 5. Parallelogram


def parallelogram(base, height):
    """
    Calculate the area of a parallelogram.

    Parameters:
    - base (float): Length of the base of the parallelogram.
    - height (float): Height of the parallelogram.

    Returns:
    float: Area of the parallelogram.
    """
    return base * height

# 6. Trapezoid


def trapezoid(base1, base2, height):
    """
    Calculate the area of a trapezoid.

    Parameters:
    - base1 (float): Length of the first base of the trapezoid.
    - base2 (float): Length of the second base of the trapezoid.
    - height (float): Height of the trapezoid.

    Returns:
    float: Area of the trapezoid.
    """
    return 0.5 * (base1 + base2) * height

# 7. Ellipse


def ellipse(major_axis, minor_axis):
    """
    Calculate the area of an ellipse.

    Parameters:
    - major_axis (float): Length of the major axis of the ellipse.
    - minor_axis (float): Length of the minor axis of the ellipse.

    Returns:
    float: Area of the ellipse.
    """
    return math.pi * major_axis * minor_axis

# 8. Rhombus


def rhombus(diagonal1, diagonal2):
    """
    Calculate the area of a rhombus.

    Parameters:
    - diagonal1 (float): Length of the first diagonal of the rhombus.
    - diagonal2 (float): Length of the second diagonal of the rhombus.

    Returns:
    float: Area of the rhombus.
    """
    return 0.5 * diagonal1 * diagonal2

# 9. Regular Polygon (n-sided)


def regular_polygon(side, n):
    """
    Calculate the area of a regular polygon.

    Parameters:
    - side (float): Length of each side of the polygon.
    - n (int): Number of sides in the polygon.

    Returns:
    float: Area of the regular polygon.
    """
    return (0.25 * n * side**2) / math.tan(math.pi / n)

# 10. Equilateral Triangle


def equilateral_triangle(side):
    """
    Calculate the area of an equilateral triangle.

    Parameters:
    - side (float): Length of each side of the equilateral triangle.

    Returns:
    float: Area of the equilateral triangle.
    """
    return (math.sqrt(3) / 4) * side**2

# 11. Isosceles Triangle


def isosceles_triangle(base, height):
    """
    Calculate the area of an isosceles triangle.

    Parameters:
    - base (float): Length of the base of the isosceles triangle.
    - height (float): Height of the isosceles triangle.

    Returns:
    float: Area of the isosceles triangle.
    """
    return 0.5 * base * height

# 12. Hexagon


def hexagon(side):
    """
    Calculate the area of a hexagon.

    Parameters:
    - side (float): Length of each side of the hexagon.

    Returns:
    float: Area of the hexagon.
    """
    return (3 * math.sqrt(3) / 2) * side**2

# 13. Pentagon


def pentagon(side, apothem):
    """
    Calculate the area of a pentagon.

    Parameters:
    - side (float): Length of each side of the pentagon.
    - apothem (float): Apothem (distance from the center to the midpoint of a side).

    Returns:
    float: Area of the pentagon.
    """
    return 0.5 * 5 * side * apothem

# 14. Kite


def kite(diagonal1, diagonal2):
    """
    Calculate the area of a kite.

    Parameters:
    - diagonal1 (float): Length of the first diagonal of the kite.
    - diagonal2 (float): Length of the second diagonal of the kite.

    Returns:
    float: Area of the kite.
    """
    return 0.5 * diagonal1 * diagonal2

# 15. Sector of a Circle


def circle_sector(radius, central_angle):
    """
    Calculate the area of a sector of a circle.

    Parameters:
    - radius (float): Radius of the circle.
    - central_angle (float): Central angle (in radians) of the sector.

    Returns:
    float: Area of the sector.
    """
    return 0.5 * radius**2 * central_angle

# 16. Annulus (Ring)


def annulus(outer_radius, inner_radius):
    """
    Calculate the area of an annulus (ring).

    Parameters:
    - outer_radius (float): Outer radius of the annulus.
    - inner_radius (float): Inner radius of the annulus.

    Returns:
    float: Area of the annulus.
    """
    return math.pi * (outer_radius**2 - inner_radius**2)

# 17. Quadrilateral (with known vertices)


def quadrilateral(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Calculate the area of a quadrilateral given its vertices.

    Parameters:
    - x1, y1, x2, y2, x3, y3, x4, y4 (float): Coordinates of the vertices of the quadrilateral.
    - y4 is not a requirment 
    Returns:
    float: Area of the quadrilateral.
    """
    return 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2) + x4*(y2 - y1))
