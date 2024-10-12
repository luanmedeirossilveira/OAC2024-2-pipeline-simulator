class Instruction:
    VALID_OPCODES = ["ADD", "SUB", "ADDI", "SUBI", "BEQ", "J"]

    def __init__(self, opcode, op1, op2=None, op3=None, valida=True):
        if opcode not in self.VALID_OPCODES:
            raise ValueError(f"Invalid opcode: {opcode}")
        self.opcode = opcode
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.valida = valida
    
    def __str__(self):
        return f"{self.opcode} {self.op1}, {self.op2}, {self.op3}"

    def __repr__(self):
        return self.__str__()
