import uuid

class Cliente:
    def __init__(self,nombre,saldo):
        self.id = uuid.uuid4()
        self.nombre = nombre                     
        self.saldo = saldo

    def girar(self,giro):
        self.saldo = self.saldo - giro

    def abonar(self,abono):
        self.saldo = self.saldo + abono

    def mostrar_saldo(self):
        print(self.nombre, " tienes un saldo de : ", self.saldo)


class Financiera:
    clientes = []    
    def __init__(self,nombre,saldo_institucional):
        self.id = uuid.uuid4()
        self.nombre = nombre                     
        self.saldo_institucional = saldo_institucional        

    def agregar_cliente(self,cliente):
        clientes = self.clientes.append(cliente)

    def eliminar_cliente(self,cliente):
        clientes = self.clientes.remove(cliente)   


cliente = Cliente("Juan Carlos Cabello",1000000)
cliente2 = Cliente("Yo",2000000)
cliente3 = Cliente("tu ahora", 1400000)
cliente4 = Cliente("Pedro ahora", 2000000)
cliente5 = Cliente("PEPE ahora", 2000000)
cliente6 = Cliente("Aurora ahora", 2000000)


financiera = Financiera("Prestamos JG",15000000)
financiera.agregar_cliente(cliente.nombre)
financiera.agregar_cliente(cliente2.nombre)
financiera.agregar_cliente(cliente3.nombre)
financiera.agregar_cliente(cliente4.nombre)
financiera.agregar_cliente(cliente5.nombre)
financiera.agregar_cliente(cliente6.nombre)

cliente4.girar(300000)
cliente4.girar(100000000)
cliente.girar(150000)
cliente2.abonar(600000)

cliente6.mostrar_saldo()

#print(cliente.nombre)
#print(cliente.saldo)
#print(cliente.id)
#print(cliente2.id)
#print(financiera.clientes)
#financiera.eliminar_cliente(cliente2.nombre)
#print(financiera.clientes)
