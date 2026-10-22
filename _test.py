import pytest

from convex_hull import convex_hull
from data_structures import Point


def hull_coordinates(points):
    polygon = convex_hull([Point(x, y) for x, y in points])
    return [(point.x, point.y) for point in polygon.vertices]


@pytest.mark.parametrize(
    ("points", "expected"),
    [
        ([], []),
        ([(2, 3)], [(2, 3)]),
        ([(3, 1), (-1, 2)], [(-1, 2), (3, 1)]),
        ([(0, 0), (4, 0), (1, 3)], [(0, 0), (4, 0), (1, 3)]),
    ],
)
def test_convex_hull_small_inputs(points, expected):
    result = hull_coordinates(points)

    assert len(result) == len(expected)
    assert set(result) == set(expected)


def test_convex_hull_excludes_interior_points():
    result = hull_coordinates(
        [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2), (1, 1), (-2, -2)]
    )

    assert set(result) == {(-2, -2), (4, 0), (4, 4), (0, 4)}
    assert len(result) == 4


def test_convex_hull_deduplicates_input_points():
    result = hull_coordinates([(0, 0), (2, 0), (0, 2), (0, 0), (2, 0)])

    assert set(result) == {(0, 0), (2, 0), (0, 2)}
    assert len(result) == 3


def test_convex_hull_of_collinear_points_contains_only_endpoints():
    result = hull_coordinates([(-2, -2), (0, 0), (1, 1), (3, 3)])

    assert set(result) == {(-2, -2), (3, 3)}
    assert len(result) == 2
