import unittest
from src.register_file import RegisterFile

class TestRegisterFile(unittest.TestCase):
    def setUp(self):
        self.reg_file = RegisterFile()

    def test_initial_values(self):
        self.assertEqual(self.reg_file.get(0), 0)

    def test_write_register(self):
        self.reg_file.set(1, 42)
        self.assertEqual(self.reg_file.get(1), 42)

if __name__ == '__main__':
    unittest.main()
