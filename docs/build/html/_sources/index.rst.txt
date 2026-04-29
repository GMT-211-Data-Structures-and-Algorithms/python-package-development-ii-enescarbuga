pa-package-1 Documentation
==========================

This project implements Point and Line classes in Python.

Features
--------

- Create Point objects
- Create Line objects
- Calculate distance between two points

Example
-------

.. code-block:: python

    from pa_package.point import Point
    from pa_package.line import Line

    p1 = Point(0, 0)
    p2 = Point(3, 4)

    line = Line(p1, p2)
    print(line.length())