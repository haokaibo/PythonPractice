class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, bottom: Point, top: Point):
        self.bottom = bottom
        self.top = top


class OverlappingRectangles:
    @staticmethod
    def get_overlap_area(rec1: Rectangle, rec2: Rectangle):
        area = 0
        y_size = min(rec1.top.y, rec2.top.y) - max(rec1.bottom.y, rec2.bottom.y)
        x_size = min(rec1.top.x, rec2.top.x) - max(rec1.bottom.x, rec2.bottom.x)
        if x_size > 0 and y_size > 0:
            area = x_size * y_size
        return area


area = OverlappingRectangles.get_overlap_area(Rectangle(Point(2, 1), Point(5, 5)),
                                              Rectangle(Point(3, 2), Point(5, 7)))
print(f'area={area}')

area = OverlappingRectangles.get_overlap_area(Rectangle(Point(1, 1), Point(3, 3)),
                                              Rectangle(Point(2, 2), Point(4, 4)))
print(f'area={area}')
