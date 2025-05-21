from persona import Persona

class Alumno(Persona):
    def _init_( # CONSTRUCTOR!
        self,
        el_nombre,
        el_apellido,
        el_dni,
        el_legajo,
    ):
        super()._init_(el_nombre, el_apellido, el_dni)
        self.legajo = el_legajo

    def _repr_(self):
        return f'Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}'
    
elio = Alumno('Elio', 'Anci', 5678567, 123443)
nick = Alumno('nick', 'peres', 56890443, 123579)

print(elio)
print(nick)