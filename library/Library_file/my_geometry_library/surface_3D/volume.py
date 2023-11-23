import math

# 1. Cube


def cube(side):
    """
    Calculate the volume of a cube.

    Parameters:
    - side (float): Length of the side of the cube.

    Returns:
    float: Volume of the cube.
    """
    return side**3

# 2. Cuboid (Rectangular Prism)


def cuboid(length, width, height):
    """
    Calculate the volume of a cuboid (rectangular prism).

    Parameters:
    - length (float): Length of the prism.
    - width (float): Width of the prism.
    - height (float): Height of the prism.

    Returns:
    float: Volume of the prism.
    """
    return length * width * height

# 3. Sphere


def sphere(radius):
    """
    Calculate the volume of a sphere.

    Parameters:
    - radius (float): Radius of the sphere.

    Returns:
    float: Volume of the sphere.
    """
    return (4/3) * math.pi * radius**3

# 4. Cylinder


def cylinder(radius, height):
    """
    Calculate the volume of a cylinder.

    Parameters:
    - radius (float): Radius of the cylinder.
    - height (float): Height of the cylinder.

    Returns:
    float: Volume of the cylinder.
    """
    return math.pi * radius**2 * height

# 5. Cone


def cone(radius, height):
    """
    Calculate the volume of a cone.

    Parameters:
    - radius (float): Radius of the cone.
    - height (float): Height of the cone.

    Returns:
    float: Volume of the cone.
    """
    return (1/3) * math.pi * radius**2 * height

# 6. Triangular Pyramid


def triangular_pyramid(base_area, height):
    """
    Calculate the volume of a triangular pyramid.

    Parameters:
    - base_area (float): Area of the pyramid base.
    - height (float): Height of the pyramid.

    Returns:
    float: Volume of the pyramid.
    """
    return (1/3) * base_area * height

# 7. Rectangular Pyramid (Cuboid)


def rectangular_pyramid(base_area, height):
    """
    Calculate the volume of a rectangular pyramid (cuboid).

    Parameters:
    - base_area (float): Area of the pyramid base.
    - height (float): Height of the pyramid.

    Returns:
    float: Volume of the pyramid.
    """
    return (1/3) * base_area * height

# 8. Cuboctahedron


def cuboctahedron(edge):
    """
    Calculate the volume of a cuboctahedron.

    Parameters:
    - edge (float): Edge length of the cuboctahedron.

    Returns:
    float: Volume of the cuboctahedron.
    """
    return (5/3) * math.sqrt(2) * edge**3

# 9. Octahedron


def octahedron(side):
    """
    Calculate the volume of an octahedron.

    Parameters:
    - side (float): Side length of the octahedron.

    Returns:
    float: Volume of the octahedron.
    """
    return (1/3) * math.sqrt(2) * side**3
