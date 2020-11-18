import uuid

saldo_institucional = 1000000


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

    def mostrar_saldo_institucional(self):
        print(self.nombre, " tienes un saldo de : ", self.saldo_institucional)



    '''
    def transferir(self, cliente):
    def giros_totales(self,):
    def abonos_totales(self,):
      
    '''
#Crear 2 Financieras

financiera1 = Financiera("Dinerobank",100000000)
financiera2 = Financiera("Credicorp",100000000)

#Crear 4 clientes por cada financiera
cliente1 = Cliente("Cliente1", 500000)
cliente2 = Cliente("Cliente2", 2000000)
cliente3 = Cliente("Cliente3", 1400000)
cliente4 = Cliente("Cliente4", 1400000)

financiera1.agregar_cliente(cliente1.nombre)
financiera1.agregar_cliente(cliente2.nombre)
financiera1.agregar_cliente(cliente3.nombre)
financiera1.agregar_cliente(cliente4.nombre)

cliente5 = Cliente("Cliente5", 100000000)
cliente6 = Cliente("Cliente6", 2000000)
cliente7 = Cliente("Cliente7", 1400000)
cliente8 = Cliente("Cliente8", 1400000)

financiera2.agregar_cliente(cliente5.nombre)
financiera2.agregar_cliente(cliente6.nombre)
financiera2.agregar_cliente(cliente7.nombre)
financiera2.agregar_cliente(cliente8.nombre)

print(financiera1.clientes)

#Realizar 3 operaciones por cada cliente de distinto tipo

 
cliente1.girar(300000)
cliente2.girar(150000)
cliente3.girar(150000)
cliente1.abonar(100000)
cliente1.mostrar_saldo()


#Realizar giros en dos clientes que demuestren que el saldo no puede ser menor a -1000000
"""
monto_girar = int(input("Ingrese el monto que desea girar:"))


if monto_girar - saldo_institucional.cliente1 <= 1000000:
    print("Su saldo es insuficiente, no puede realizar giros")

else:
        print("giro aprobado")

#Transferencias     






#print(cliente.nombre)
#print(cliente.saldo)
#print(cliente.id)
#print(cliente2.id)
print(financiera.clientes)
financiera.eliminar_cliente(cliente2.nombre)
print(financiera.clientes)

"""