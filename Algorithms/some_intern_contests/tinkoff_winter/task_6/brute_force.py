from itertools import combinations

def is_non_degenerate(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) != (p3[0] - p1[0]) * (p2[1] - p1[1])

def solve(n, points):
    valid_triangles = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_non_degenerate(points[i], points[j], points[k]):
                    valid_triangles.append((i, j, k))
    
    # Sort triangles by some heuristic (e.g., perimeter)
    def triangle_perimeter(t):
        return sum(abs(points[t[i]][0] - points[t[j]][0]) + abs(points[t[i]][1] - points[t[j]][1]) 
                   for i, j in [(0,1), (1,2), (2,0)])
    
    valid_triangles.sort(key=triangle_perimeter, reverse=True)
    
    def backtrack(index, used_mask, count):
        if count * 3 + n - bin(used_mask).count('1') < count * 3:
            return count
        
        if index == len(valid_triangles):
            return count
        
        current_triangle = valid_triangles[index]
        triangle_mask = (1 << current_triangle[0]) | (1 << current_triangle[1]) | (1 << current_triangle[2])
        
        if used_mask & triangle_mask == 0:
            include = backtrack(index + 1, used_mask | triangle_mask, count + 1)
        else:
            include = 0
        
        exclude = backtrack(index + 1, used_mask, count)
        
        return max(include, exclude)
    
    return backtrack(0, 0, 0)

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(n, points))

if __name__ == "__main__":
    main()