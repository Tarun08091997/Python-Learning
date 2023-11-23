import math

# 1. Cube


def cube(side):
    """
    Calculate the surface area of a cube.

    Parameters:
    - side (float): Length of the side of the cube.

    Returns:
    float: Surface area of the cube.
    """
    return 6 * side**2

# 2. Rectangular Prism (or Cuboid)


def cuboid(length, width, height):
    """
    Calculate the surface area of a rectangular prism (or cuboid).

    Parameters:
    - length (float): Length of the prism.
    - width (float): Width of the prism.
    - height (float): Height of the prism.

    Returns:
    float: Surface area of the prism.
    """
    return 2 * (length * width + length * height + width * height)

# 3. Sphere


def sphere(radius):
    """
    Calculate the surface area of a sphere.

    Parameters:
    - radius (float): Radius of the sphere.

    Returns:
    float: Surface area of the sphere.
    """
    return 4 * math.pi * radius**2

# 4. Cylinder


def cylinder(radius, height):
    """
    Calculate the surface area of a cylinder.

    Parameters:
    - radius (float): Radius of the cylinder.
    - height (float): Height of the cylinder.

    Returns:
    float: Surface area of the cylinder.
    """
    return 2 * math.pi * radius * (radius + height)

# 5. Cone


def cone(radius, slant_height):
    """
    Calculate the surface area of a cone.

    Parameters:
    - radius (float): Radius of the cone.
    - slant_height (float): Slant height of the cone.

    Returns:
    float: Surface area of the cone.
    """
    return math.pi * radius * (radius + slant_height)

# 6. Triangular Pyramid


def triangular_pyramid(base_perimeter, slant_height, base_area):
    """
    Calculate the surface area of a triangular pyramid.

    Parameters:
    - base_perimeter (float): Perimeter of the pyramid base.
    - slant_height (float): Slant height of the pyramid.
    - base_area (float): Area of the pyramid base.

    Returns:
    float: Surface area of the pyramid.
    """
    return 0.5 * base_perimeter * slant_height + base_area

# 7. Rectangular Pyramid


def rectangular_pyramid(base_perimeter, slant_height, base_area):
    """
    Calculate the surface area of a rectangular pyramid.

    Parameters:
    - base_perimeter (float): Perimeter of the pyramid base.
    - slant_height (float): Slant height of the pyramid.
    - base_area (float): Area of the pyramid base.

    Returns:
    float: Surface area of the pyramid.
    """
    return base_perimeter * slant_height + base_area

# 8. Cuboctahedron


def cuboctahedron(edge):
    """
    Calculate the surface area of a cuboctahedron.

    Parameters:
    - edge (float): Edge length of the cuboctahedron.

    Returns:
    float: Surface area of the cuboctahedron.
    """
    return 14 * edge**2

# 9. Octahedron


def octahedron(side):
    """
    Calculate the surface area of an octahedron.

    Parameters:
    - side (float): Side length of the octahedron.

    Returns:
    float: Surface area of the octahedron.
    """
    return 2 * math.sqrt(3) * side**2
