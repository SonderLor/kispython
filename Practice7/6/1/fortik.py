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


if __name__ == "__main__":
    disassemble([0, 16, 16, 1, 121, 5])
