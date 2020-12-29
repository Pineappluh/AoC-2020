import fileinput


class Code:

    def __init__(self, instructions):
        self.instructions = instructions
        self.executed = []
        self.accumulator = 0
        self.next_instruction = 0

    def run(self):
        contains_loop = False
        while self.next_instruction < len(self.instructions) and not contains_loop:
            contains_loop = self.run_next_instruction()

    def run_next_instruction(self):
        if self.next_instruction in self.executed:
            return True

        self.executed.append(self.next_instruction)

        instruction = self.instructions[self.next_instruction]
        i_name, i_value = instruction.split()
        i_value = int(i_value)
        offset = 1

        if i_name == "nop":
            pass
        elif i_name == "acc":
            self.accumulator += i_value
        elif i_name == "jmp":
            offset = i_value

        self.next_instruction += offset
        return False


instructions = []
for line in fileinput.input():
    instructions.append(line.strip())

code = Code(instructions)
code.run()
print(code.accumulator)

