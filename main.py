from data_structures import Point
from convex_hull import convex_hull


def main():
    # Example usage of the convex hull algorithm
    points = [
        Point(0, 0),
        Point(1, 1),
        Point(2, 2),
        Point(0, 2),
        Point(2, 0),
        Point(1, 0.5),
    ]

    # Compute the convex hull
    convex_hull_polygon = convex_hull(points)

    # Print the result
    print("Convex Hull Vertices:")
    for vertex in convex_hull_polygon.vertices:
        print(vertex)


if __name__ == "__main__":
    main()
