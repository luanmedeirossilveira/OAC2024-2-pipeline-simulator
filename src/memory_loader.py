from src.instruction import Instruction

def load_program(file_path):
    instructions = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()

            if not parts:
                continue

            opcode = parts[0]

            if opcode in ['ADD', 'SUB'] or opcode == 'BEQ':
                op1, op2, op3 = int(parts[1]), int(parts[2]), int(parts[3])
                instructions.append(Instruction(opcode, op1, op2, op3))
            elif opcode in ['ADDI', 'SUBI']:
                op1, op2, op3 = int(parts[1]), int(parts[2]), None
                instructions.append(Instruction(opcode, op1, op2, op3))
            elif opcode == 'J':
                op1 = int(parts[1])
                instructions.append(Instruction(opcode, op1, None, None))
            else:
                raise ValueError(f"Opcode desconhecido: {opcode}")

    return instructions
