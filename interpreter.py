class Interpreter:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.tape = bytearray(300_000)
        self.head = 0

    def interpret(self, program: str, arg: bytearray | None) -> bytearray:
        program_head = 0
        input_head = 0
        bracket_stack = []
        bracket_tail = len(program)
        while program_head < len(program):
            match program[program_head]:
                case ">":
                    self.head += 1
                case "<":
                    self.head -= 1
                case "+":
                    self.tape[self.head] += 1
                case "-":
                    self.tape[self.head] -= 1
                case ".":
                    print(bytes([self.tape[self.head]]).decode('utf-8'))
                case ",":
                    if input_head >= len(arg):
                        self.tape[self.head] = 0
                    else:
                        self.tape[self.head] = arg[input_head]
                        input_head += 1
                case "[":
                    if not bracket_stack or bracket_stack[-1] != program_head:
                        bracket_stack.append(program_head)
                    if self.tape[self.head] == 0:
                        program_head = bracket_tail
                        continue
                case "]":
                    self.bracket_tail = program_head
                    if self.tape[self.head] == 0:
                        if not bracket_stack:
                            raise Exception("missing matching [")
                        bracket_stack.pop(-1)
                    else:
                        program_head = bracket_stack[-1]
                        continue
                case _:
                    raise Exception("disallowed character!")
            program_head += 1
        return self.tape