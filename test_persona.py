import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from persona import Persona, Profesor, Alumno

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.pepe = Persona('Pepe', 'Garcia', 34563456)

    def test_creacion_persona(self):
        self.assertEqual(self.pepe.nombre, 'Pepe')
        self.assertEqual(self.pepe.apellido, 'Garcia')
        self.assertEqual(self.pepe.dni, 34563456)
        self.assertEqual(self.pepe.ultima_idea, '<no penso en nada>')

    def test_pensar(self):
        self.pepe.pensar('Pelota')
        self.assertEqual(self.pepe.ultima_idea, 'Pelota')
        self.assertEqual(self.pepe.pensamientos, 1)

class TestProfesor(unittest.TestCase):
    def setUp(self):
        self.gabriel = Profesor('Gabriel', 'Flores', 12341234, 111111111)

    def test_creacion_profesor(self):
        self.assertEqual(self.gabriel.nombre, 'Gabriel')
        self.assertEqual(self.gabriel.apellido, 'Flores')
        self.assertEqual(self.gabriel.dni, 111111111)
        self.assertEqual(self.gabriel.sueldo, 12341234)

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