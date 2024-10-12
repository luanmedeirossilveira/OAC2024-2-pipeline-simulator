import unittest
from src.instruction import Instruction

class TestInstruction(unittest.TestCase):
    def test_add_instruction(self):
      instruction = Instruction("ADD", 1, 2, 3)
      self.assertEqual(instruction.op1, 1)
      self.assertEqual(instruction.op2, 2)
      self.assertEqual(instruction.op3, 3)

    def test_invalid_instruction(self):
        with self.assertRaises(ValueError):
            Instruction("INVALID", 1, 2, 3)

if __name__ == '__main__':
    unittest.main()
