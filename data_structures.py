class Point:
    """
    A representation of a point in 2D space with x and y coordinates.
    """

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Polygon:
    """
    A representation of a polygon in 2D space with a list of vertices.
    """

    vertices: list[Point]

    def __init__(self, vertices: list[Point]):
        self.vertices = vertices

    def __str__(self):
        return f"{', '.join(str(v) for v in self.vertices)}"

    def area(self) -> float:
        """
        Calculate the area of the polygon using the Shoelace formula. Assumes the vertices are ordered clockwise or counter-clockwise.
        """

        n = len(self.vertices)
        if n < 3:
            return 0.0  # Not a polygon

        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += self.vertices[i].x * self.vertices[j].y
            area -= self.vertices[j].x * self.vertices[i].y
        return abs(area) / 2.0
