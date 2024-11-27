class TuringMachine:
    def __init__(self, tape, initial_state, bls='0'): # bls = blank symbol
        self.tape = list(tape)
        self.head_position = 0
        self.current_state = initial_state
        self.blank_symbol = bls
        self.rules = {
            ('q0', '0'): ('0', 'R', 'q0'),  
            ('q0', '1'): ('1', 'R', 'q0'), 
            ('q0', bls): (bls, 'L', 'q1'),
            ('q1', '0'): ('1', 'L', 'q3'),
            ('q1', 'q'): ('0', 'L', 'HALT'),
        }

    def step(self):
        if self.current_state == 'HALT':
            return False

        current_symbol = self.tape[self.head_position] if self.head_position < len(self.tape) else self.blank_symbol
        action = self.rules.get((self.current_state, current_symbol))

        if action:
            write_symbol, move_direction, next_state = action
            if self.head_position < len(self.tape):
                self.tape[self.head_position] = write_symbol
            elif write_symbol != self.blank_symbol:
                self.tape.append(write_symbol)

            self.current_state = next_state

            if move_direction == 'R':
                self.head_position += 1
            elif move_direction == 'L':
                self.head_position -= 1
                if self.head_position < 0:
                    self.tape.insert(0, self.blank_symbol)
                    self.head_position = 0

            # Print the current state of the Turing machine
            print(f"State: {self.current_state}, Head Position: {self.head_position}, Tape: {''.join(self.tape)}")

            return True
        else:
            return False

    def run(self):
        counter = 0
        while self.step() and counter < 100:  # Maximum number of steps
            counter += 1
            pass

    def get_tape(self):
        # Remove leading and trailing blank symbols
        return ''.join(self.tape).strip(self.blank_symbol)


# Example usage
tape = "10111"
tm = TuringMachine(tape, 'q0', bls='B')  # Using 'B' as the blank symbol
print("Initial tape:", tape)
tm.run()
print("Final Tape:", tm.get_tape())
print("Final State:", tm.current_state)