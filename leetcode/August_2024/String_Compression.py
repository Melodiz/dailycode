class Solution:
    def compress(self, chars) -> int:
        last_char = chars[0]
        count = 1
        index = 0
        for char in chars[1:]:
            if char == last_char:
                count += 1
            else:
                chars[index] = last_char
                index += 1
                if count > 1:
                    for digit in str(count):
                        chars[index] = digit
                        index += 1
                last_char = char
                count = 1
        chars[index] = last_char
        index += 1
        if count > 1:
            for digit in str(count):
                chars[index] = digit
                index += 1
        return index