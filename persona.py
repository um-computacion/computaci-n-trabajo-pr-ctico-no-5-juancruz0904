class Persona:
    def _init_( # CONSTRUCTOR!
        self,
        el_nombre,
        el_apellido,
        el_dni,
    ):
        self.nombre = el_nombre
        self.apellido = el_apellido
        self.dni = el_dni
        self.pensamientos = 0
        self.ultima_idea = '<no penso en nada>'

    def pensar(self, idea):
        self.pensamientos += 1
        self.ultima_idea = idea

    def _repr_(self):
        return f'La Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}'


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


gabriel = Profesor('Gabriel', 'Flores', 12341234, 111111111)
daniel = Profesor('Daniel', 'Quinteros', 224352345, 20000000)
pepe = Persona('Pepe', 'Garcia', 34563456)
elio = Alumno('Elio', 'Anci', 5678567, 1234)


pepe.pensar('Pelota')
pepe.pensar('Chiste')
pepe.pensar('Nada..')
pepe.pensar('Muerte...')

gabriel.pensar('Futbol')

print(elio)
print(gabriel)
print(daniel)
print(pepe)