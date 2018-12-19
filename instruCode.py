def instru(code, A, B, C, registers):
    if code == 'addr':
        registers[C] = registers[A] + registers[B]
        return registers
    elif code == 'addi':
        registers[C] = registers[A] + B
        return registers
    elif code == 'mulr':
        registers[C] = registers[A] * registers[B]
        return registers
    elif code == 'muli':
        registers[C] = registers[A] * B
        return registers
    elif code == 'banr':
        if registers[A] and registers[B]:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers
    elif code == 'bani':
        if registers[A] and B:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers
    elif code == 'borr':
        if registers[A] or registers[B]:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers
    elif code == 'bori':
        if registers[A] or B:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers
    elif code == 'setr':
        registers[C] = registers[A]
        return registers
    elif code == 'seti':
        registers[C] = A
        return registers
    elif code == 'gtir':
        if A > registers[B]:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers
    elif code == 'gtri':
        if registers[A] > B:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers
    elif code == 'gtrr':
        if registers[A] > registers[B]:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers
    elif code == 'eqir':
        if A == registers[B]:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers
    elif code == 'eqri':
        if registers[A] == B:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers
    elif code == 'eqrr':
        if registers[A] == registers[B]:
            registers[C] = 1
        else:
            registers[C] = 0
        return registers