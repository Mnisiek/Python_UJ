import pytest

from points import Point
from rectangles import Rectangle


def test_create_rect():
    rect = Rectangle(2, 0, 8, 4)
    assert rect.left == 2
    assert rect.bottom == 0
    assert rect.right == 8
    assert rect.top == 4
    assert rect.width == 6
    assert rect.height == 4

def test_create_from_points():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    rect = Rectangle.from_points((p1, p2))
    assert rect.left == 1
    assert rect.bottom == 2
    assert rect.right == 3
    assert rect.top == 4

def test_virtual_attributes():
    rect = Rectangle(1, 1, 4, 5)
    assert rect.topleft == Point(1, 5)
    assert rect.bottomleft == Point(1, 1)
    assert rect.topright == Point(4, 5)
    assert rect.bottomright == Point(4, 1)
    assert rect.center == Point(2.5, 3)

def test_area():
    rect = Rectangle(0, 1, 4, 5)
    assert rect.area() == 16

def test_intersection():
    rect1 = Rectangle(0, 0, 4, 4)
    rect2 = Rectangle(2, 2, 6, 6)
    inter = rect1.intersection(rect2)
    assert inter == Rectangle(2, 2, 4, 4)

def test_cover():
    rect1 = Rectangle(0, 0, 4, 4)
    rect2 = Rectangle(2, 2, 6, 6)
    cover = rect1.cover(rect2)
    assert cover == Rectangle(0, 0, 6, 6)

def test_make4():
    rect = Rectangle(0, 0, 4, 4)
    sub_rects = rect.make4()
    assert sub_rects[0] == Rectangle(0, 2, 2, 4)
    assert sub_rects[1] == Rectangle(2, 2, 4, 4)
    assert sub_rects[2] == Rectangle(2, 0, 4, 2)
    assert sub_rects[3] == Rectangle(0, 0, 2, 2)
