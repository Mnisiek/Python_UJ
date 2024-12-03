"""
Wzbogacić klasę Rectangle o nowe funkcjonalności (plik rectangles.py).

Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć prostokąt
z listy lub krotki zawierającej dwa punkty, lewy dolny i prawy górny. Wywołanie:
rectangle = Rectangle.from_points((point1, point2))

Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę
(współrzędną tylko do odczytu): top, left, bottom, right, width, height.
Dodać atrybuty wirtualne zwracające Point (tylko do odczytu): topleft,
bottomleft, topright, bottomright. Można rozważyć zamianę metody
center() na atrybut wirtualny.

W osobnym pliku (test_rectangles.py) przygotować testy klasy Rectangle
w formacie dla modułu 'pytest'. """


from points import Point


class Rectangle:
    """Klasa reprezentująca prostkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Nieprawidłowe wymiary prostkąta.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
        if len(points) != 2:
            raise ValueError("Lista musi zawierać dokładnie dwa elementy.")
        p1, p2 = points
        return cls(p1.x, p1.y, p2.x, p2.y)

    def __str__(self):
        return f"[({self.pt1.x, self.pt1.y}), ({self.pt2.x, self.pt2.y})]"
    
    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    
    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2
    
    def __ne__(self, other):
        return not self == other
    
    @property
    def center(self):
        return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)
    
    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x
    
    @property
    def width(self):
        return self.pt2.x - self.pt1.x
    
    @property
    def height(self):
        return self.pt2.y - self.pt1.y
    
    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        return self.pt1

    @property
    def topright(self):
        return self.pt2

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)
    
    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)
    
    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self
    
    def intersection(self, other):
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        else:
            raise ValueError("Brak części wspólnej")
    
    def cover(self, other):
        # min/max odwrotnie niż do szukania części wspólnej
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)
    
    def make4(self):
        # A-------B   po podziale  A---+---B
        # |       |                |   |   |
        # |       |                +---+---+
        # |       |                |   |   |
        # D-------C                D---+---C
        center = self.center
        rect1 = Rectangle(self.left, center.y, center.x, self.top)
        rect2 = Rectangle(center.x, center.y, self.right, self.top)
        rect3 = Rectangle(center.x, self.bottom, self.right, center.y)
        rect4 = Rectangle(self.left, self.bottom, center.x, center.y)
        return rect1, rect2, rect3, rect4
