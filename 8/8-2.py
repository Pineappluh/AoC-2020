import fileinput


class Code:

    def __init__(self, instructions):
        self.instructions = instructions
        self.executed = []
        self.accumulator = 0
        self.next_instruction = 0

    def run(self):
        self.accumulator = 0
        self.next_instruction = 0
        self.executed = []
        contains_loop = False
        while self.next_instruction < len(self.instructions) and not contains_loop:
            contains_loop = self.run_next_instruction()

        return contains_loop

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

    def fix_loop(self):
        try_corrupted = 0
        while True:
            tmp_instructions = self.instructions.copy()
            while not self.instructions[try_corrupted][:3] in ["nop", "jmp"]:
                try_corrupted += 1

            if self.instructions[try_corrupted].startswith("nop"):
                self.instructions[try_corrupted] = self.instructions[try_corrupted].replace("nop", "jmp")
            else:
                self.instructions[try_corrupted] = self.instructions[try_corrupted].replace("jmp", "nop")

            contains_loop = self.run()
            if not contains_loop:
                return

            self.instructions = tmp_instructions
            try_corrupted += 1


instructions = []
for line in fileinput.input():
    instructions.append(line.strip())

code = Code(instructions)
code.fix_loop()
code.run()
print(code.accumulator)

