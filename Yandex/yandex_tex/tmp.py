# Examine my solution:
def Solution(points) -> bool:
    min_x, max_x = float('inf'), float('-inf')
    points_set = set()
    for x, y in points:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        points_set.add((x, y))
    t2x0 = min_x+max_x
    for x, y in points:
        # check if there is a reflected point; 
        x_pair = t2x0-x
        if (x_pair, y) not in points_set: return False
    return True

