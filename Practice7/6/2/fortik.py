OPERATION_NAMES = {
    0: 'push',
    1: 'op',
    2: 'call',
    3: 'is',
    4: 'to',
    5: 'exit'
}


def not_implemented(vm):
    raise RuntimeError('Not implemented!')


LIBRARY = {
    '+': not_implemented,
    '-': not_implemented,
    '*': not_implemented,
    '/': not_implemented,
    '%': not_implemented,
    '&': not_implemented,
    '|': not_implemented,
    '^': not_implemented,
    '<': not_implemented,
    '>': not_implemented,
    '=': not_implemented,
    '<<': not_implemented,
    '>>': not_implemented,
    'if': not_implemented,
    'for': not_implemented,
    '.': not_implemented
}


def disassemble(commands):
    print("entry:")
    for command in commands[1:]:
        mask = 7
        operation = OPERATION_NAMES[command & mask]
        argument = command >> 3

        if operation == 'op':
            argument = f"'{list(LIBRARY.keys())[argument]}'"

        print(f"\t{operation} {argument}")


class VM:
    def __init__(self, code):
        self.stack = []
        self.code = code
        self.pc = 0

    def run(self):
        while self.pc < len(self.code):
            command = self.code[self.pc]
            operation = command & 7
            argument = command >> 3
            operation = OPERATION_NAMES[operation]
            if operation == 'push':
                self.stack.append(argument)
            elif operation == 'op':
                op_name = list(LIBRARY.keys())[argument]
                LIBRARY[op_name](self)
            elif operation == 'exit':
                break
            self.pc += 1

    def op_add(self):
        if len(self.stack) < 2:
            raise RuntimeError("Not enough operands on the stack for addition")
        a = self.stack.pop()
        b = self.stack.pop()
        result = a + b
        self.stack.append(result)

    def op_dot(self):
        if len(self.stack) < 1:
            raise RuntimeError("No value to print")
        value = self.stack.pop()
        print(value)


def main() -> None:
    LIBRARY['+'] = lambda vm: vm.op_add()
    LIBRARY['.'] = lambda vm: vm.op_dot()

    bytecode = [0, 16, 16, 1, 121, 5]
    disassemble(bytecode)
    vm = VM(bytecode)
    vm.run()
    print()
    bytecode = [0, 24, 80, 1, 121, 5]
    disassemble(bytecode)
    vm = VM(bytecode)
    vm.run()


if __name__ == "__main__":
    main()
