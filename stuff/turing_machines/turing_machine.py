class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)
        self.head = 0
        self.state = 'start'
        self.period_length = 1

    def step(self):
        if self.state == 'start':
            if self.period_length >= len(self.tape):
                self.state = 'reject'
            else:
                self.state = 'check_period'
                self.head = 0

        elif self.state == 'check_period':
            if self.head + self.period_length < len(self.tape):
                if self.tape[self.head] == self.tape[self.head + self.period_length]:
                    self.head += 1
                else:
                    self.state = 'next_period'
            else:
                self.state = 'accept'

        elif self.state == 'next_period':
            self.period_length += 1
            self.state = 'start'

    def run(self):
        while self.state not in ['accept', 'reject']:
            self.step()
        return self.state

# Example usage
word = "bbab"
tm = TuringMachine(word)
result = tm.run()
print(f"The word '{word}' is {'periodic' if result == 'accept' else 'not periodic'}.")