from persona import Persona

class Profesor(Persona):
    def _init_( # CONSTRUCTOR!
        self,
        el_nombre,
        el_apellido,
        el_sueldo,
        el_dni,
    ):
        super()._init_(el_nombre, el_apellido, el_dni)
        self.sueldo = el_sueldo

    def _repr_(self):
        return f'Este Profesor: DNI: {self.dni} Nombre y Apellido: {self.nombre} , {self.apellido} tiene un sueldo: {self.sueldo}'

tom = Profesor('tom', 'gomes', 120000, 15240940)
maxi = Profesor('maxi', 'martines', 100500, 20235780)

print(tom)
print(maxi)