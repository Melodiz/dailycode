class Solution:
    def isReflected(self, points) -> bool:
        maxX, minX = float('-inf'), float('inf')
        set_points = set()
        for x, y in points:
            maxX = max(maxX,x)
            minX = min(minX,x)
            set_points.add((x, y))
        lineX = maxX + minX
        return all((lineX-x, y) in set_points for x, y in points)
