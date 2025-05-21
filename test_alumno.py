import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from persona import Alumno

class TestAlumno(unittest.TestCase):
    def setUp(self):
        self.elio = Alumno('Elio', 'Anci', 5678567, 1234)

    def test_creacion_alumno(self):
        self.assertEqual(self.elio.nombre, 'Elio')
        self.assertEqual(self.elio.apellido, 'Anci')
        self.assertEqual(self.elio.dni, 5678567)
        self.assertEqual(self.elio.legajo, 1234)

if __name__ == '_main_':
    unittest.main()