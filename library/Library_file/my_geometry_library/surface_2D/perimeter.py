import math


def rectangle(length, width):
    """
    Calculate the perimeter of a rectangle.

    Parameters:
    - length (float): Length of the rectangle.
    - width (float): Width of the rectangle.

    Returns:
    float: Perimeter of the rectangle.
    """
    return 2 * (length + width)


def square(side):
    """
    Calculate the perimeter of a square.

    Parameters:
    - side (float): Side length of the square.

    Returns:
    float: Perimeter of the square.
    """
    return 4 * side


def circle(radius):
    """
    Calculate the circumference of a circle.

    Parameters:
    - radius (float): Radius of the circle.

    Returns:
    float: Circumference of the circle.
    """
    return 2 * math.pi * radius


def triangle(side1, side2, side3):
    """
    Calculate the perimeter of a triangle.

    Parameters:
    - side1 (float): Length of the first side of the triangle.
    - side2 (float): Length of the second side of the triangle.
    - side3 (float): Length of the third side of the triangle.

    Returns:
    float: Perimeter of the triangle.
    """
    return side1 + side2 + side3


def parallelogram(side1, side2):
    """
    Calculate the perimeter of a parallelogram.

    Parameters:
    - side1 (float): Length of the first side of the parallelogram.
    - side2 (float): Length of the second side of the parallelogram.

    Returns:
    float: Perimeter of the parallelogram.
    """
    return 2 * (side1 + side2)


def trapezoid(base1, base2, side1, side2):
    """
    Calculate the perimeter of a trapezoid.

    Parameters:
    - base1 (float): Length of the first base of the trapezoid.
    - base2 (float): Length of the second base of the trapezoid.
    - side1 (float): Length of the first non-base side of the trapezoid.
    - side2 (float): Length of the second non-base side of the trapezoid.

    Returns:
    float: Perimeter of the trapezoid.
    """
    return base1 + base2 + side1 + side2


def ellipse(major_axis, minor_axis):
    """
    Calculate the perimeter (approximation) of an ellipse.

    Parameters:
    - major_axis (float): Length of the major axis of the ellipse.
    - minor_axis (float): Length of the minor axis of the ellipse.

    Returns:
    float: Perimeter (approximation) of the ellipse.
    """
    a, b = major_axis / 2, minor_axis / 2
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))


def rhombus(side):
    """
    Calculate the perimeter of a rhombus.

    Parameters:
    - side (float): Length of the side of the rhombus.

    Returns:
    float: Perimeter of the rhombus.
    """
    return 4 * side


def regular_polygon(side, n):
    """
    Calculate the perimeter of a regular polygon.

    Parameters:
    - side (float): Length of each side of the polygon.
    - n (int): Number of sides in the polygon.

    Returns:
    float: Perimeter of the regular polygon.
    """
    return n * side


def equilateral_triangle(side):
    """
    Calculate the perimeter of an equilateral triangle.

    Parameters:
    - side (float): Length of each side of the equilateral triangle.

    Returns:
    float: Perimeter of the equilateral triangle.
    """
    return 3 * side


def isosceles_triangle(base, side):
    """
    Calculate the perimeter of an isosceles triangle.

    Parameters:
    - base (float): Length of the base of the isosceles triangle.
    - side (float): Length of each equal side of the isosceles triangle.

    Returns:
    float: Perimeter of the isosceles triangle.
    """
    return 2 * side + base


def hexagon(side):
    """
    Calculate the perimeter of a hexagon.

    Parameters:
    - side (float): Length of each side of the hexagon.

    Returns:
    float: Perimeter of the hexagon.
    """
    return 6 * side


def pentagon(side):
    """
    Calculate the perimeter of a pentagon.

    Parameters:
    - side (float): Length of each side of the pentagon.

    Returns:
    float: Perimeter of the pentagon.
    """
    return 5 * side


def kite(side1, side2):
    """
    Calculate the perimeter of a kite.

    Parameters:
    - side1 (float): Length of the first side of the kite.
    - side2 (float): Length of the second side of the kite.

    Returns:
    float: Perimeter of the kite.
    """
    return 2 * (side1 + side2)


def sector_of_a_circle(radius, central_angle):
    """
    Calculate the arc length (approximation) of a sector of a circle.

    Parameters:
    - radius (float): Radius of the circle.
    - central_angle (float): Central angle (in radians) of the sector.

    Returns:
    float: Arc length (approximation) of the sector.
    """
    return radius * central_angle


def annulus(outer_radius, inner_radius):
    """
    Calculate the perimeter (approximation) of an annulus (ring).

    Parameters:
    - outer_radius (float): Outer radius of the annulus.
    - inner_radius (float): Inner radius of the annulus.

    Returns:
    float: Perimeter (approximation) of the annulus.
    """
    return 2 * math.pi * (outer_radius + inner_radius)


def quadrilateral(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Calculate the perimeter of a quadrilateral given its vertices.

    Parameters:
    - x1, y1, x2, y2, x3, y3, x4, y4 (float): Coordinates of the vertices of the quadrilateral.

    Returns:
    float: Perimeter of the quadrilateral.
    """
    side1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    side2 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    side3 = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
    side4 = math.sqrt((x1 - x4)**2 + (y1 - y4)**2)
    return side1 + side2 + side3 + side4
