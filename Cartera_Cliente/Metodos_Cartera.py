import os
from Crud_Archivo import Archivo
from Clases_Entidades import *

def borrarPantalla():
    os.system("cls")


def Clientes():
    archivo = Archivo("cliente")
    try:
        with open(f"archivos/{archivo.nombrearchivo}.txt", 'r') as f:
            lines = f.readlines()
            idCodigo = len(lines) + 1
    except FileNotFoundError:
        idCodigo = 1
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese la cedula del cliente: ")
    estado = input("Ingrese el estado del cliente: ")
    cliente = Cliente(idCodigo, nombre, estado, cedula)
    archivo.agregar_elemento(cliente.mostrarDatos())
#Cliente, factura, credito[pago], pago
def mostrarCliente():
    cliente_codigo = input("Ingrese el código del cliente que desea consultar: ")
    archivo_cliente = Archivo("cliente")
    resultado = archivo_cliente.buscar_elemento_lista(cliente_codigo)
    if resultado == f"No se encuentra el elemento en la lista":
        print("El código del cliente no existe.")
    else:
        print(resultado)
        idCodigo, nombre, estado, cedula = resultado[0], resultado[1], resultado[2], resultado[3]
        cliente = Cliente(idCodigo, nombre, estado, cedula)
        print(cliente.mostrarDatos())


def Facturas():
    cliente_codigo = input("Ingrese el código del cliente: ")
    archivo_cliente = Archivo("cliente")
    resultado = archivo_cliente.buscar_elemento_lista(cliente_codigo)
    if resultado == f"No se encuentra el elemento en la lista":
        print("El código del cliente no existe.")
        return
    else:
        idCodigo, nombre, estado, cedula = resultado[0], resultado[1], resultado[2], resultado[3]
        cliente = Cliente(idCodigo, nombre, estado, cedula)
        print("Cliente: ",nombre)
        archivo_factura = Archivo("factura")
        try:
            with open(f"archivos/{archivo_factura.nombrearchivo}.txt", "r") as f:
                facturas = f.readlines()
                idFactura = len(facturas) + 1
        except FileNotFoundError:
            with open(f"archivos/{archivo_factura.nombrearchivo}.txt", "w") as f:
                idFactura = 1
        fecha = input("Ingrese la fecha de la factura: ")
        total = input("Ingrese el total de la factura: ")
        estado = input("Ingrese el estado de la factura: ")
        factura = Factura(str(idFactura), cliente, fecha, total, estado)
        archivo_factura.agregar_elemento(factura.mostrarDatos())


def mostrarFactura():
    factura_codigo = input("Ingrese el código de la factura que desea consultar: ")
    archivo_factura = Archivo("factura")
    resultado = archivo_factura.buscar_elemento_lista(factura_codigo)
    if resultado == "No se encuentra el elemento en la lista":
        print("El código de la factura no existe.")
    else:
        idFactura, fecha, total, cliente, estado = resultado[0], resultado[1], resultado[2], resultado[3], resultado[4]
        cliente = Cliente("",cliente,"","")
        factura = Factura(idFactura, cliente, fecha, total, estado)
        print(factura.mostrarDatos())


def Pagos():
    archivo = Archivo("pago")
    try:
        idPago = len(archivo.leer_archivo()) + 1
    except FileNotFoundError:
        with open(f"archivos/{archivo.nombrearchivo}.txt", "w") as f:
            pass
        idPago = 1
    fechapago = input("Ingrese la fecha de pago: ")
    valor = input("Ingrese el valor: $")
    pago = Pago(idPago, fechapago, valor)
    archivo.agregar_elemento(str(pago.mostrarDato()))

def mostrarPago():
    pago_codigo = input("Ingrese el código del pago que desea consultar: ")
    archivo_pago = Archivo("pago")
    resultado = archivo_pago.buscar_elemento_lista(pago_codigo)
    if resultado == f"No se encuentra el elemento en la lista":
        print("El código del pago no existe.")
        return
    else:
        idPago, fechaPago, valor = resultado
        print(f"Código de pago: {idPago}")
        print(f"Fecha de pago: {fechaPago}")
        print(f"Valor: {valor}")

def Detalles_Credito():
    borrarPantalla()
    print("="*20)
    print(" "*8,"Detalles"," "*8)
    print("="*20)
    codigo_pago = input("Ingrese el código del pago: ")
    archivo_pago = Archivo("pago")
    resultado = archivo_pago.buscar_elemento_lista(codigo_pago)
    if resultado == f"No se encuentra el elemento en la lista":
        print("El código del pago no se encuentra en los registros.")
        return
    else:
        idPago, fechapago, valor = resultado[0], resultado[1], resultado[2]
        pago = Pago(idPago, fechapago, valor)
        print("Valor: $",valor)
        archivo_detalle = Archivo("detcredito")
        try:
            with open(f"archivos/{archivo_detalle.nombrearchivo}.txt", "r") as f:
                detalles = f.readlines()
                idDetCredito = len(detalles) + 1
        except FileNotFoundError:
            with open(f"archivos/{archivo_detalle.nombrearchivo}.txt", "w") as f:
                idDetCredito = 1
        aamm = input("Ingrese la fecha de pago: ")
        cuota = input("Ingrese el valor de la cuota: $")
        estado = input("Ingrese el estado del pago: ")
        det = DetCredito(idDetCredito, aamm, cuota, estado)
        archivo_detalle.agregar_elemento(det.mostrarDatos())


def Credito():
    try:
        with open(f"archivos/pago.txt", 'r') as f:
            pass  
    except FileNotFoundError:
        input("Primero debes agregar un pago\nPulse una tecla para continuar... ")
        return
    codigo_factura = input("Ingrese el codigo de la factura: ")
    archivo_factura = Archivo("factura")
    resultado = archivo_factura.buscar_elemento_lista(codigo_factura)
    if resultado == f"No se encuentra el elemento en la lista":
        print("El código de la factura no se encuentra en los registros.")
        return
    else:
        idFactura, fecha, total, cliente, estado = resultado[0], resultado[1], resultado[2], resultado[3], resultado[4]
        factura = Factura(idFactura, cliente, fecha, total, estado)
        print(f"Codigo Factura: {idFactura} Cliente:{cliente} Total: {total}")
        archivo_credito = Archivo(f"credito")
        try:
            with open(f"archivos/{archivo_credito.nombrearchivo}.txt", "r") as f:
                detalles = f.readlines()
                idCredito = len(detalles) + 1
        except FileNotFoundError:
            with open(f"archivos/{archivo_credito.nombrearchivo}.txt", "w") as f:
                idCredito = 1   
        print(f"Codigo: {idCredito}")    
        fecha = input("Ingrese la fecha: ")
        deuda = input("Ingrese el valor de la deuda: $")
        numeroCuota = input("Ingrese el N° Cuota: ")
        cuotas = input("Ingrese el valor cuota: $")
        ammm = input("Ingrese la fecha inicial de pago: ")
        credito = CabCredito(idCredito, factura, fecha, deuda, numeroCuota, cuotas, ammm, estado)
        archivo_credito.agregar_elemento(credito.mostrarDato())
        for i in range(int(numeroCuota)):
            Detalles_Credito()
        input("Registro guardado con exito....\nPulse una tecla para continuar... ")

def mostrarCredito():
    credito_codigo = input("Ingrese el código de la deuda que desea consultar: ")
    archivo_credito = open("archivos/credito.txt", "r")
    lineas = archivo_credito.readlines()
    encontrado = False
    for linea in lineas:
        campos = linea.strip().split(",")
        if campos[0] == credito_codigo:
            encontrado = True
            idCabCredito, factura, fecha, deuda, numeroCuota, cuota, aammInicial, estado = campos[0], campos[1], campos[2], campos[3], campos[4], campos[5], campos[6], campos[7]
            print(f"Código de la deuda: {idCabCredito}  Codigo Factura: {factura}")
            print(f"Fecha: {fecha}             Deuda: {deuda}")
            print(f"Número de cuota: {numeroCuota}      Cuota: {cuota}")
            print(f"Año y mes inicial: {aammInicial}    Estado: {estado}")
            print(f"\nDetalles de crédito:")
            print(f"idDetCredito  Fecha Pago  Cuota  Estado")
            archivoDetallecredito = Archivo("detcredito")
            lineasDetalleCredito = archivoDetallecredito.leer_archivo()
            for lineaDetalleCredito in lineasDetalleCredito:
                idDetCredito, aamm, cuotaDet, estadoDet = lineaDetalleCredito.strip().split(",")
                print(f"{idDetCredito}            {aamm}    {cuotaDet}  {estadoDet}")
    if not encontrado:
        print("El código de la deuda no existe.")
    archivo_credito.close()