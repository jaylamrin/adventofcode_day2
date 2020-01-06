
def run_program(program: list, noun: int = None, verb: int = None) -> int:
    if noun:
        program[1] = noun
    if verb:
        program[2] = verb

    for x in range(0, len(program), 4):
        opcode = program[x]
        if opcode == 1:
            program[program[x+3]] = program[program[x+1]] + \
                program[program[x+2]]
        elif opcode == 2:
            program[program[x+3]] = program[program[x+1]] * \
                program[program[x+2]]
        elif opcode == 99:
            break
        else:
            print(f'Invalid opcode')
    return program[0]


with open('day2.txt', 'r') as text_file:
    mylist = text_file.read().split(',')
mylist = [int(s) for s in mylist]

#print(run_program(mylist, 0, 1))

for noun in range(0, 100, 1):
    for verb in range(0, 100, 1):
        trylist = mylist.copy()
        if run_program(trylist, noun, verb) == 19690720:
            print(100 * noun + verb)
            break
