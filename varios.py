# from colorama import Fore, Back, Style, init

# init(autoreset=True)

# print(Back.LIGHTMAGENTA_EX + "Este texto es rojo")
# print(Style.LIGHTMAGENTA_EX + "Este texto es rojo")

from faker import Faker

fake = Faker("es_CO")

class Usuario:
    def __init__(self, nombre, email, telefono, direccion):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        pass
    
    def __str__(self):
        return f"Nombre: {self.nombre} | Email {self.email} | Telefono : {self.telefono} | direccion: {self.direccion}"
        pass
    
for i in range(10):
    usuario = Usuario(fake.name(),fake.email(),fake.phone_number(),fake.address(),)
    print(usuario)
    print("==============================")


# print(fake.name())
# print(fake.email())
# print(fake.phone_number())
# print(fake.address())