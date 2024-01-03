import numpy as np
import math


def sq_euclidean_distance(a, b):
    """
    Computes squared Euclidean distance
    given two two-dimentional points
    """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def closest_split_pair(Px, Py, delta):
    """
    Identify closest split pairs and return them and the distance
    :param Px: Two dimentional array sorted by x
    :param Py: Two dimentional array sorted by y
    :param delta: min distance from righ or left halves
    """

    n = len(Px) // 2
    x = Px[n][0]
    lower_bound = x - delta
    upper_bound = x + delta
    Sy = []
    best_pair = (np.nan, np.nan)
    for p in Py:
        if lower_bound <= p[0] <= upper_bound:
            Sy.append(p)

    for i in range(len(Sy)):
        for j in range(i + 1, len(Sy)):
            distance = sq_euclidean_distance(Sy[i], Sy[j])
            if distance < delta:
                best_pair = (Sy[i], Sy[j])
                delta = distance

    return best_pair, delta


def sort_list(points):
    """
    Sort two dimentional array by x, and y-coordinates
    :param points:
    :return:
    """
    Px = sorted(points, key=lambda x: x[0])
    Py = sorted(points, key=lambda x: x[1])
    return Px, Py


def brute_force(Px):
    """
    Brute force routine when there are 3 or less pairs

    :param Px: two-dimensional array
    :return:
    """
    d1 = sq_euclidean_distance(Px[0], Px[1])
    p1 = Px[0]
    p2 = Px[1]
    ln_ax = len(Px)
    if ln_ax == 2:
        return (p1, p2), d1

    for i in range(ln_ax):
        for j in range(i + 1, ln_ax):
            d = sq_euclidean_distance(Px[i], Px[j])
            if d < d1:
                d1 = d
                p1, p2 = Px[i], Px[j]
    return (p1, p2), d1


def closest_pair(Px, Py):
    """
    Closest pair algorithm based on divide and conquer

    :param Px: two-dimensional array sorted by x-coordinate
    :param Py: two-dimensional array sorted by x-coordinate
    :return:
    """
    # the base case
    if len(Px) <= 3:
        return brute_force(Px)

    # Divide into left and right halves and call the fun recursively
    n = len(Px) // 2
    Qx = Px[:n]
    Qx_x_points = [i[0] for i in Qx]
    Rx = Px[n:]
    Qy = []
    Ry = []
    for it in Py:
        if it[0] in Qx_x_points:
            Qy.append(it)
        else:
            Ry.append(it)

    l_closest, l_delta = closest_pair(Qx, Qy)
    r_closest, r_delta = closest_pair(Rx, Ry)

    if l_delta < r_delta:
        c_pair = l_closest
        delta = l_delta
    else:
        c_pair = r_closest
        delta = r_delta
    s_closest, s_delta = closest_split_pair(Px, Py, delta)
    if s_delta < delta:
        delta = s_delta
        c_pair = s_closest
    return c_pair, delta
