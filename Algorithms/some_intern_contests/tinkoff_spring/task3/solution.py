# def solve(data_string, req_alp, max_length):
#     n_alpf_power = len(req_alp)
#     cur_letters = {}
#     cur_freques = {0: n_alpf_power}
#     for letter in req_alp:
#         cur_letters[letter] = 0
#     reset_letters = cur_letters.copy()
#     l, r = 0, 0
#     left_most_index = 0
#     result = (0, 0)
#     while r < len(data_string):
#         # if not all letters in substring
#         if cur_freques[0] > 0:
#             cfq = cur_letters[data_string[r]]
#             cur_freques[cfq] -= 1
#             cur_freques[cfq+1] = cur_freques.get(cfq+1, 0) + 1
#             cur_letters[data_string[r]] += 1
#             if l == left_most_index:
#                 result = (l, r) 
#             r += 1
#         # case all is good
#         elif data_string[r] in req_alp and r-l < max_length:
#             cfq = cur_letters[data_string[r]]
#             cur_freques[cfq] -= 1
#             cur_freques[cfq+1] = cur_freques.get(cfq+1, 0) + 1
#             cur_letters[data_string[r]] += 1
#             if l == left_most_index:
#                 result = (l, r)
#             r += 1
#         # case r is in req_alp but length is greater than max_length
#         elif data_string[r] in req_alp:
#             # move the left pointer
#             l += 1
#             cur_freques[cur_letters[data_string[l]]-1] += 1
#             cur_letters[data_string[l]] -= 1
#             # check if all letters still in substring
#             if cur_freques[0] > 0:
#                 break
#             # now the string in valid
#             if l > left_most_index:
#                 left_most_index = l
#                 result = (l, r-1)
#             # if we break the loop, than the string is valid now
#         # case if r is not in req_alp but the length is ok
#         elif data_string[r] not in req_alp and r-l < max_length:
#             # move the left pointer until we can and than reset the substring
#             # keep in mind that the r now is not valid, so the r - 1 is last valid index
#             if l >= left_most_index:  # maybe that's never the useful case
#                 left_most_index = l
#                 result = (l, r-1)
#             while l < r:  # in fact that would never reached
#                 l += 1
#                 cur_freques[cur_letters[data_string[l]]-1] += 1
#                 cur_letters[data_string[l]] -= 1
#                 if cur_freques[0] > 0:  # not valid now, so reset and break
#                     r = r+1  # since r is not in valid, there is no need to check
#                     l = r
#                     cur_freques[0] = n_alpf_power
#                     cur_letters = reset_letters.copy()
#                     break
#                 # still valid, so update the result
#                 if l >= left_most_index:
#                     left_most_index = l
#                     result = (l, r-1)
#         # case if r is not in req_alp and the length is greater than max_length
#         else:
#             # move the left pointer until we can and than reset the substring
#             # keep in mind that the r now is not valid, so the r - 1 is last valid index
#             while l - r > max_length:
#                 l += 1
#                 cur_freques[cur_letters[data_string[l]]-1] += 1
#                 cur_letters[data_string[l]] -= 1
#                 if cur_freques[0] > 0:  # not valid now, so reset and break
#                     r = r+1  # since r is not in valid, there is no need to check
#                     l = r
#                     cur_freques[0] = n_alpf_power
#                     cur_letters = reset_letters.copy()
#                     break
#             # now the lenght is ok, so we move to tne case above
#             pass
#     # the r is reached the end of string, so we need to check the last substrings
#     # if l >= left_most_index:  # maybe that's never the useful case
#     #     left_most_index = l
#     #     result = (l, r-1) if r-l+1 <= max_length else "None5"
#     while l < len(data_string):  # in fact that would never reached
#         l += 1
#         cur_freques[cur_letters[data_string[l]]-1] += 1
#         cur_letters[data_string[l]] -= 1
#         if cur_freques[0] > 0:  # not valid now, so reset and break
#             return data_string[result[0]:result[1]+1]
#         # still valid, so update the result
#         if l >= left_most_index:
#             left_most_index = l
#             result = (l, r-1)
#     return ''

def solve(data_string, allowed, maxLength):
    dict1 = {}
    set1 = set(allowed)
    ans = (None, None)
    for key in list(set1):
        dict1[key] = dict1.get(key, 0) + 1
    l = 0
    def check(dict1, keys):
        empty = True
        for item in dict1:
            # if (item in set1 and dict1[item] > 0) or (item not in keys and dict1[item]!=0):
            #     empty = False
            #     break
            if (item in set1) and dict1[item] > 0:
                empty = False
                break
            elif (item not in set1 and dict1[item]!=0):
                empty = False
                break
        return empty
    for r in range(len(data_string)):
        bukva = data_string[r]
        if bukva not in set1:
            while l <= r:
                if check(dict1, allowed):
                    ans = (l, r-1)
                if data_string[l] in set1:
                    dict1[data_string[l]]+=1
                l+=1
            # for j in range(l, r):
            #     if nabor[j] in set1:
            #         dict1[nabor[j]]+=1
            # l = r
            # continue
        else:
            dict1[bukva]-=1
        if check(dict1, allowed):
            ans = (l, r)
        # while l < r and check(dict1, keys):
        #     if nabor[l] in set1:
        #         dict1[nabor[l]] = dict1.get(nabor[l], 0) + 1
        #     l+=1
        #     ans = (l, l+maxLength)
        if (r-l+1) == maxLength:
            if data_string[l] in dict1:
                dict1[data_string[l]]+=1
                l+=1
    while l <= r and check(dict1, allowed):
        ans = (l, l+maxLength)
        if data_string[l] in dict1:
            dict1[data_string[l]]+=1
        l+=1
    #print(ans)
    left, right = ans
    if left is None:
        return -1
    else:
        for i in range(right+1, min(r+maxLength, len(bukva))):
            if data_string[i] in set1:
                right+=1
        return data_string[left:right+1]


def main():
    data_string = input()
    req_alp = input()
    max_length = int(input())
    if len(req_alp) > max_length:
        print(-1)
    else:
        print(solve(data_string, req_alp, max_length))


if __name__ == "__main__":
    main()