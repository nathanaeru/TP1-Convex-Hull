from math import atan2

from data_structures import Point, Polygon


def order_clockwise(points: list[Point]) -> list[Point]:
    """
    Orders a list of points in clockwise order around their centroid.
    """

    if not points:
        return []

    # Calculate the centroid of the points
    centroid_x = sum(p.x for p in points) / len(points)
    centroid_y = sum(p.y for p in points) / len(points)

    # Sort points based on their angle with respect to the centroid
    def angle_from_centroid(point: Point) -> float:
        return atan2(point.y - centroid_y, point.x - centroid_x)

    return sorted(points, key=angle_from_centroid, reverse=True)


def _y_value_at_x(first: Point, second: Point, x: float) -> float:
    """
    Returns the y-coordinate where the segment intersects the vertical line x.
    """
    if first.x == second.x:
        return (first.y + second.y) / 2
    return first.y + (second.y - first.y) * (x - first.x) / (second.x - first.x)


def merge_hulls(left: list[Point], right: list[Point]) -> list[Point]:
    """
    Merges two convex hulls into a single convex hull. Assumes that the input hulls are ordered clockwise.
    """

    if not left:
        return right
    if not right:
        return left

    # Find the rightmost point of the left hull and the leftmost point of the right hull
    left_index = max(range(len(left)), key=lambda i: left[i].x)
    right_index = min(range(len(right)), key=lambda i: right[i].x)

    x = (left[left_index].x + right[right_index].x) / 2
    i, j = left_index, right_index

    # Walk around both hulls to find the upper tangent.
    while True:
        previous_i = (i - 1) % len(left)
        next_j = (j + 1) % len(right)
        current_y = _y_value_at_x(left[i], right[j], x)

        if _y_value_at_x(left[previous_i], right[j], x) > current_y:
            i = previous_i
        elif _y_value_at_x(left[i], right[next_j], x) > current_y:
            j = next_j
        else:
            break

    upper_i, upper_j = i, j
    i, j = left_index, right_index

    # Walk around both hulls to find the lower tangent.
    while True:
        next_i = (i + 1) % len(left)
        previous_j = (j - 1) % len(right)
        current_y = _y_value_at_x(left[i], right[j], x)

        if _y_value_at_x(left[next_i], right[j], x) < current_y:
            i = next_i
        elif _y_value_at_x(left[i], right[previous_j], x) < current_y:
            j = previous_j
        else:
            break

    # Collect the points from the upper tangent to the lower tangent
    lower_i, lower_j = i, j
    merged_points = [left[upper_i], right[upper_j]]

    while upper_j != lower_j:
        upper_j = (upper_j + 1) % len(right)
        merged_points.append(right[upper_j])

    while lower_i != upper_i:
        merged_points.append(left[lower_i])
        lower_i = (lower_i + 1) % len(left)

    return merged_points


def convex_hull(points: list[Point]) -> Polygon:
    """
    Computes the convex hull of a set of points using the Divide and Conquer algorithm.
    """

    # Sort points by x-coordinate, then by y-coordinate if x-coordinates are equal.
    points = sorted(points, key=lambda p: (p.x, p.y))
    unique_points = []
    for point in points:
        if not unique_points or (point.x, point.y) != (
            unique_points[-1].x,
            unique_points[-1].y,
        ):
            unique_points.append(point)
    points = unique_points

    if len(points) > 2 and all(
        (point.x - points[0].x) * (points[-1].y - points[0].y)
        == (point.y - points[0].y) * (points[-1].x - points[0].x)
        for point in points[1:-1]
    ):
        return Polygon([points[0], points[-1]])

    # Base case: construct a consistently ordered hull for small inputs.
    if len(points) <= 3:
        return Polygon(order_clockwise(points))

    # Divide the points into two halves
    mid = len(points) // 2
    left_hull = convex_hull(points[:mid])
    right_hull = convex_hull(points[mid:])

    # Merge the child hull boundaries, ignoring interior vertices and duplicates.
    merged_hull = merge_hulls(left_hull.vertices, right_hull.vertices)
    return Polygon(order_clockwise(merged_hull))
