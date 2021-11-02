

class Uno(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar(self):
        print(self.nombre, self.apellido)


class Dos(Uno):

    def __init__(self, nombre, apellido, direccion):
        super().__init__(nombre, apellido)
        self.direccion = direccion

    def mostrar(self):
        print(self.nombre, self.apellido, self.direccion)

    def enviar_correo(self, mail):
        print('enviar mail a', mail)


class Tres(Uno):
    
    def __init__(self, nombre, apellido, mail):
        super().__init__(nombre, apellido)
        self.mail = mail

    def mostrar(self):
        print(self.nombre, self.apellido, self.mail)

    def caminiar(self, mail):
        print('enviar mail a', mail)



p = Uno('hola', 'chau')
# p.mostrar()

r = Dos('111', '222', '3333')
r2 = Tres('aaaa', 'bbb', 'ccc')
# r.enviar_correo('asdas@asdasd.com')



lista = [p, r, r2]

for elemento in lista:
    elemento.mostrar()
