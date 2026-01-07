# Solution for https://leetcode.com/problems/implement-queue-using-stacks/
# Other solutions: https://github.com/Melodiz/dailycode/tree/main/leetcode

from typing import List, Optional
class MyQueue:

    def __init__(self):
        self.s1 = [] # For pushing
        self.s2 = [] # For popping/peeking

    def push(self, x: int) -> None:
        # Always push to the input stack
        self.s1.append(x)

    def pop(self) -> int:
        # Ensure s2 has the current front of the queue
        self.move_s1_to_s2()
        return self.s2.pop()

    def peek(self) -> int:
        # Ensure s2 has the current front of the queue
        self.move_s1_to_s2()
        return self.s2[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        return not self.s1 and not self.s2

    def move_s1_to_s2(self) -> None:
        # Only transfer if s2 is empty to maintain correct FIFO order
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

def run_tests():
    passed, failed = 0, 0
    
    # Test cases: (input_args, expected_output)
    test_cases = [
        ((["MyQueue","push","push","peek","pop","empty"], [[],[1],[2],[],[],[]]), None),  # TODO: Add expected output
    ]
    
    for (commands, inputs), expected in test_cases:
        try:
            obj = None
            results = []
            for cmd, inp in zip(commands, inputs):
                if cmd == "MyQueue":
                    obj = MyQueue(*inp)
                    results.append(None)
                elif obj:
                    res = getattr(obj, cmd)(*inp)
                    results.append(res)
            
            if expected is not None:
                if results == expected:
                    passed += 1
                else:
                    failed += 1
                    print(f"✗ FAIL: Input={(commands, inputs)}, Expected={expected}, Got={results}")
            else:
                print(f"Output: {results} (Input: {(commands, inputs)})")
        except Exception as e:
            failed += 1
            print(f"✗ ERROR: Input={(commands, inputs)}, Error={e}")
    
    if failed == 0 and passed > 0:
        print("OK")
    elif passed == 0 and failed == 0:
        print("No test cases to run")

if __name__ == "__main__":
    run_tests()
