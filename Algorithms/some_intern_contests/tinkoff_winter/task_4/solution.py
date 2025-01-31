def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

def cost_to_multiple(num, val):
    r = num % val
    if r == 0:
        return 0
    return val - r

def opt_solution(n, x, y, z, a):

    # Precompute all relevant LCMs
    lcm_xy = lcm(x, y)
    lcm_xz = lcm(x, z)
    lcm_yz = lcm(y, z)
    lcm_xyz = lcm(lcm_xy, z)

    # minCost[c] = minimal cost over all elements to make an element cover subset c
    # bit representation: 1->x, 2->y, 4->z
    INF = 10**20
    minCost = [INF]*8  # we'll use indices 1..7

    for val in a:
        cX  = cost_to_multiple(val, x)
        cY  = cost_to_multiple(val, y)
        cZ  = cost_to_multiple(val, z)
        cXY = cost_to_multiple(val, lcm_xy)
        cXZ = cost_to_multiple(val, lcm_xz)
        cYZ = cost_to_multiple(val, lcm_yz)
        cXYZ= cost_to_multiple(val, lcm_xyz)
        
        # Update minimum for each coverage pattern
        minCost[1] = min(minCost[1], cX)
        minCost[2] = min(minCost[2], cY)
        minCost[3] = min(minCost[3], cXY)
        minCost[4] = min(minCost[4], cZ)
        minCost[5] = min(minCost[5], cXZ)
        minCost[6] = min(minCost[6], cYZ)
        minCost[7] = min(minCost[7], cXYZ)

    dp = [INF]*8
    dp[0] = 0

    for mask in range(8):
        if dp[mask] == INF:
            continue
        for c in range(1, 8):
            new_mask = mask | c
            dp[new_mask] = min(dp[new_mask], dp[mask] + minCost[c])

    return dp[7]

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    result = opt_solution(n, x, y, z, a)
    print(result)

if __name__ == "__main__":
    main()