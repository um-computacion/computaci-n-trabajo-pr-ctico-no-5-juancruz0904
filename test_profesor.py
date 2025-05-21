import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from persona import Profesor

class TestProfesor(unittest.TestCase):
    def setUp(self):
        self.gabriel = Profesor('Gabriel', 'Flores', 123412340, 111111111)

    def test_creacion_profesor(self):
        self.assertEqual(self.gabriel.nombre, 'Gabriel')
        self.assertEqual(self.gabriel.apellido, 'Flores')
        self.assertEqual(self.gabriel.dni, 111111111)
        self.assertEqual(self.gabriel.sueldo, 12341234)

if __name__ == '_main_':
    unittest.main()