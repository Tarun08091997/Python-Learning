"""
my_geometry_library.2D

A Python module for 2D geometric calculations, offering functions to compute the area and perimeter of various shapes.

Features:
-Rectangle
-Square
-Circle
-Triangle
-Parallelogram
-Trapezoid
-Ellipse
-Rhombus
-Regular Polygon (n-sided)
-Equilateral Triangle
-Isosceles Triangle
-Hexagon
-Pentagon
-Kite
-Sector of a Circle
-Annulus (Ring)
-Quadrilateral (with known vertices)

Usage:
Import the module and use the provided functions to perform 2D geometric calculations.

Example:
```python
from geometry_2d_module import 2D

# Rectangle calculations
rectangle_area = 2D.area.rectangle(5, 8)
rectangle_perimeter = 2D.perimeter.rectangle(5, 8)
"""
from . import area
from . import perimeter
