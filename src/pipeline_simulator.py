class PipelineSimulator:
    def __init__(self, program_memory, register_file):
        self.program_memory = program_memory
        self.register_file = register_file
        self.pipeline = [None] * 5
        self.pc = 0
        self.cycles_with_prediction = 0
        self.cycles_without_prediction = 0
    
    def load_instructions(self, instructions):
        self.program_memory = instructions
    
    def get_register_value(self, reg_num):
        return self.register_file.get(reg_num)

    def fetch(self):
        """Estágio de Busca (IF - Instruction Fetch)"""
        if self.pc < len(self.program_memory):
            instruction = self.program_memory[self.pc]
            self.pipeline[0] = instruction
            print(f"Fetch: {instruction}")
            self.pc += 1
        else:
            print("Fetch: Nenhuma instrução a buscar")
            self.pipeline[0] = None

    def decode(self):
        """Estágio de Decodificação (ID - Instruction Decode)"""
        instruction = self.pipeline[1]
        if instruction:
            opcode = instruction.opcode
            op1 = instruction.op1
            op2 = instruction.op2
            op3 = instruction.op3
            self.pipeline[1] = (opcode, op1, op2, op3)
            print(f"Decode: Opcode: {opcode}, Operandos: {op1}, {op2}, {op3}")


    def execute(self):
        """Estágio de Execução (EX - Execution)"""
        instruction = self.pipeline[2]
        if instruction is None:
            return
        if instruction:
            opcode, dest, op2, op3 = instruction
            print(f"Execute: {instruction}")
            if opcode == "ADD":
                result = self.register_file.get(op2) + self.register_file.get(op3)
                self.pipeline[2] = (opcode, dest, result)
            elif opcode == "SUB":
                result = self.register_file.get(op2) - self.register_file.get(op3)
                self.pipeline[2] = (opcode, dest, result)
            else:
                print(f"Erro: Instrução {opcode} não suportada na execução.")


    def memory(self):
        """Estágio de Memória (MEM - Memory)"""
        instruction = self.pipeline[3]
        if instruction is None:
            return
        if isinstance(instruction, tuple):
            if len(instruction) == 3:
                opcode, dest, result = instruction
                print(f"Memory: Opcode: {opcode}, Dest: {dest}, Result: {result}")
                self.pipeline[3] = (opcode, dest, result)
            else:
                print(f"Erro: Formato inesperado da instrução {instruction}")
        else:
            print(f"Erro: Instrução no estágio de memória não é uma tupla: {instruction}")

    def write_back(self):
        """ Estágio de Escrever no Banco de Registradores (WB - Write Back) """
        instruction = self.pipeline[-1]
        if instruction is None:
            return
        if isinstance(instruction, tuple):
            if len(instruction) == 3:
                opcode, dest, result = instruction
                if opcode in ["ADD", "SUB"] and dest != 0:
                    self.register_file[dest] = result
                else:
                    print(f"Erro: Formato inesperado da instrução {instruction} no estágio Write Back")
            elif len(instruction) == 2:  # ADDI, SUBI, etc
                opcode, dest = instruction
                print(f"Write-back para {opcode} no registrador {dest}")
        else:
            print(f"Erro: Formato inesperado da instrução {instruction} no estágio Write Back")

    def run(self):
        """Executa o pipeline"""
        while self.pc < len(self.program_memory) or any(self.pipeline):
            self.write_back()
            self.memory()    
            self.execute()   
            self.decode()    
            self.fetch()     

            self.pipeline = [None] + self.pipeline[:-1]
            self.cycles_with_prediction += 1
            print(f"Ciclo (com predição) {self.cycles_with_prediction} completo\n")

    def run_without_prediction(self):
        """Executa o pipeline sem predição de desvios"""
        self.pc = 0
        self.pipeline = [None] * 5
        print("#################################################")
        while self.pc < len(self.program_memory) or any(self.pipeline):            
            if self.pipeline[2]:
                opcode = self.pipeline[2][0]
                if opcode == "BEQ":
                    print("Desvio condicional encontrado, inserindo bolhas (sem predição)")
                    self.pipeline = [None] * 2 + self.pipeline[:-2]
                    self.cycles_without_prediction += 2

            self.write_back()
            self.memory()    
            self.execute()   
            self.decode()    
            self.fetch()     

            self.pipeline = [None] + self.pipeline[:-1]
            self.cycles_without_prediction += 1
            print(f"Ciclo (sem predição) {self.cycles_without_prediction} completo\n")
