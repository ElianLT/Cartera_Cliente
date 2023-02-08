from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, idCodigo, nombre, estado):
        self.idCodigo = idCodigo
        self.nombre = nombre
        self.estado = estado
    @abstractmethod
    def mostrarDatos(self):
        pass

class Cliente(Persona):
    def __init__(self,idCodigo, nombre, estado, cedula):
        super().__init__(idCodigo, nombre, estado)
        self.cedula = cedula
    def mostrarDatos(self):
        return f"{self.idCodigo}, {self.nombre}, {self.cedula}, {self.estado}"

class Factura:
    def __init__(self, idFactura, cliente, fecha, total, estado):
        self.idFactura = idFactura
        self.cliente = cliente
        self.fecha = fecha
        self.total = total
        self.estado = estado
    def mostrarDatos(self):
        return f"{self.idFactura}, {self.fecha}, {self.total}, {self.cliente.nombre}, {self.estado}"

class Calculo(ABC):
    @abstractmethod
    def realizarPago(self):
        pass

class Pago(Calculo):
    def __init__(self, idPago, fechaPago, valor):
        self.idPago = idPago
        self.fechaPago = fechaPago
        self.valor = valor
    def mostrarDato(self):
        return f"{self.idPago}, {self.fechaPago}, {self.valor}"
    def realizarPago(self, deuda):
        self.valor -= deuda
        return self.valor

class DetCredito:
    def __init__(self, idDetCredito, aamm, cuota, estado):
        self.idDetCredito = idDetCredito
        self.aamm = aamm
        self.cuota = cuota
        self.detPago = []
        self.estado = estado
    def agregarPago(self, idPago, fechaPago, valor):
        pago = Pago(idPago, fechaPago, valor)
        self.detPago.append(pago)
    def mostrarDatos(self):
        return f"{self.idDetCredito}, {self.aamm}, {self.cuota}, {self.estado}"


class CabCredito:
    def __init__(self, idCabCredito, factura, fecha, deuda, numeroCuota, cuota, aammInicial, estado):
        self.idCabCredito = idCabCredito
        self.factura = factura
        self.fecha = fecha
        self.deuda = deuda
        self.numeroCuota = numeroCuota
        self.cuota = cuota
        self.aammInicial = aammInicial
        self.detCredito = []
        self.estado = estado
    def agregarDetalle(self, idDetCredito, aamm, cuota, estado):
        detCredito = DetCredito(idDetCredito, aamm, cuota, estado)
        self.detCredito.append(detCredito)
    def mostrarDato(self):
        return f"{self.idCabCredito}, {self.factura.idFactura}, {self.fecha}, {self.deuda}, {self.numeroCuota}, {self.cuota}, {self.aammInicial}, {self.estado}"
























        # print("="*25, "Detalle", "="*25)
        # print("Codigo    Fecha Inicial    Cuota     Estado")
        # for det in self.detCredito:
        #     print(" {} {} {} {}".format(det.idDetCredito, det.aamm, det.cuota, det.estado))
        #     for pago in det.detPago:
        #         print(pago.mostrarDato())
''' 
det = DetCredito(1,"2022-02","4500",True)
det.agregarPago(10,"2022-02-02","1500")
print(det.mostrarDatos()) '''

''' cli = Cliente(1, "Steven",True, "0948848949")
factura = Factura(1, cli, "20-01-2023","2000", True)
credito = CabCredito(1, factura, "24-01-2022","3000",3,"1000","2022-02",True)
credito.agregarDetalle(1,"2022-02","1000",True)
credito.agregarDetalle(2,"2022-02","1000",True)
credito.agregarDetalle(3,"2022-02","1000",True)
print(credito.obtenerDeuda()) '''