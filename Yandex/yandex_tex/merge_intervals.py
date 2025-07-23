def solve(intervals):
    intervals.sort(key = lambda x: (x[0], -x[1]))
    ans = []
    cur_left, cur_right = intervals[0]
    for left, right in intervals[1:]:
        if left <= cur_right:
            cur_right = max(right, cur_right)
        else: # left > cur_right
            ans.append([cur_left, cur_right])
            cur_left, cur_right = left, right
    ans.append([cur_left, cur_right])
    return ans



if __name__ == "__main__":
    print(solve([[1,3], [2, 6], [8, 10], [15, 18]]))