"""
my_geometry_library

A Python library for geometric calculations, providing functions to compute the area, perimeter, and volume of various shapes.

Features:
- Rectangle calculations: area and perimeter
- Circle calculations: area and circumference
- Sphere calculations: surface area and volume

Usage:
Import the library and use the provided functions to perform geometric calculations.

Example:
```python

from geometry_2d_module import 2D
from my_geometry_library import 3D

# Rectangle calculations
rectangle_area = 2D.area.rectangle(5, 8)
rectangle_perimeter = 2D.perimeter.rectangle(5, 8)


# Cube calculations
cube_volume = 3D.volume.cube(side)
cube_surface_area = 3D.surfaceArea.cube(side)

"""

from . import surface_2D
from . import surface_3D

# Version
__version__ = 0.5
