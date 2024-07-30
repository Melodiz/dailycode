class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            curr_temperature = temperatures[i]

            while stack and curr_temperature >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result

