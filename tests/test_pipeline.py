import unittest
from src.pipeline_simulator import PipelineSimulator
from src.instruction import Instruction
from src.register_file import RegisterFile

class TestPipeline(unittest.TestCase):
    def setUp(self):
        register_file = RegisterFile()
        program_memory = []  #
        self.simulator = PipelineSimulator(program_memory, register_file)

    def test_run_with_add(self):
        instructions = [
            Instruction("ADD", 1, 2, 3),
            Instruction("SUB", 4, 5, 6)
        ]
        self.simulator.load_instructions(instructions)
        self.simulator.run_without_prediction()
        self.assertEqual(self.simulator.get_register_value(1), 0)

if __name__ == '__main__':
    unittest.main()
