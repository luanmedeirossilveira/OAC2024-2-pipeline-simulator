class RegisterFile:
    def __init__(self):
        self.registers = [0] * 32

    def get(self, reg_index):
        """Retorna o valor do registrador dado o índice"""
        if 0 <= reg_index < len(self.registers):
            return self.registers[reg_index]
        else:
            raise IndexError(f"Registrador {reg_index} fora do intervalo")

    def set(self, reg_index, value):
        """Define um valor no registrador dado o índice"""
        if 0 <= reg_index < len(self.registers):
            self.registers[reg_index] = value
        else:
            raise IndexError(f"Registrador {reg_index} fora do intervalo")
        
    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.set(index, value)
