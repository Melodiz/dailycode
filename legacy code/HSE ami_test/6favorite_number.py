inp = list(map(int, input().split()))
N,A = inp[0], inp[1]
data = [(int(input())) for t in range(N)]

all_poss_vars = set([data[0]])

for num in data[1:]:
    arr = list(all_poss_vars)
    for p_num in arr:
        all_poss_vars.add(p_num+num)
        all_poss_vars.add(p_num-num)

print(all_poss_vars)

# так как гарантируется, что sum(data)<10^4, если abs(int(input()))
for dif in range(2*10**4):
    if A-dif in all_poss_vars:
        print(A-dif)
        break
    elif A+dif in all_poss_vars:
        print(A+dif)
        break