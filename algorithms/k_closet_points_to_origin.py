import math


def k_closest_points(points, k):
    distances = [(math.sqrt(x ** 2 + y ** 2), (x, y)) for x, y in points]
    print(distances)
    # distances.sort(key=lambda x: x[0])
    return [point for _, point in distances[:k]]


print(k_closest_points([[1, 3], [-2, 2]], 1))

# How can I solve this using heap pq


