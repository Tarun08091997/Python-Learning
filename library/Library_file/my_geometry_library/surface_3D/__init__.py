"""
my_geometery_library.3D

3D Geometry Module

A Python module for 3D geometric calculations, offering functions to compute the volume and surface area of various 3D shapes.

Supported 3D Shapes:
1. Cube
2. Rectangular Prism (or Cuboid)
3. Sphere
4. Cylinder
5. Cone
6. Triangular Pyramid
7. Rectangular Pyramid
8. Cuboctahedron
9. Octahedron

Usage:
Import the module and use the provided functions to perform 3D geometric calculations.

Example:
```python
from my_geometry_library import 3D

# Cube calculations
cube_volume = 3D.volume.cube(side)
cube_surface_area = 3D.surfaceArea.cube(side)

"""
from . import surfaceArea
from . import volume
