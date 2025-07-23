def line_reflations(points) -> bool:
    # we need to determine if there is a line parallel to y-axis
    # such what each point has it's mirrored pair
    unique_points = set()
    max_x, min_x = float('-inf'), float('inf')
    for x, y in points:
        max_x, min_x = max(max_x, x), min(min_x, x)
        unique_points.add((x, y))
    twice_x0 = min_x + max_x
    for x, y in unique_points:
        if (twice_x0-x, y) not in unique_points: return False
    return True