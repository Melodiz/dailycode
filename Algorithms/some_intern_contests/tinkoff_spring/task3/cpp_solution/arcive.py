# def solution(data_string, alphabet_set, max_length):
#     substrings = set()
#     max_left = -1
#     n = len(data_string)
    
#     for left in range(n):
#         char_count = {}
#         unique_chars = 0
#         for right in range(left, min(left + max_length, n)):
#             char = data_string[right]
#             if char not in alphabet_set:
#                 break
#             if char not in char_count:
#                 char_count[char] = 0
#                 unique_chars += 1
#             char_count[char] += 1
#             sub_string = data_string[left:right + 1]
#             if unique_chars == len(alphabet_set):
#                 if left > max_left:
#                     substrings = {sub_string}
#                     max_left = left
#                 elif left == max_left:
#                     substrings.add(sub_string)
    
#     if len(substrings) == 0:
#         return -1
#     return sorted(list(substrings), key=len, reverse=True)[0]
