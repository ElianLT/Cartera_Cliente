from Componentes import Menu
from Clases_Entidades import *
from Metodos_Cartera import *


opc=''
while opc !='6':  
    borrarPantalla()
    menu = Menu("Menu Cuentas Por Cobrar",["1) Clientes","2) Facturas","3) Creditos","4) Pago", "5) Consulta General", "6) Salir"])
    opc = menu.menu()
    if opc == "1":
        borrarPantalla()
        Clientes()
    elif opc == "2":
        borrarPantalla()
        Facturas()
    elif opc == "3":
        borrarPantalla()
        try:
            Credito()
        except FileNotFoundError:
            input("Primero debes agregar un pago\nPulse una tecla para continuar... ")
    elif opc == "4":
        borrarPantalla()
        Pagos()
    elif opc == "5":
        borrarPantalla()
        menu4 = Menu("Consulta General",["1) Clientes","2) Factura", "3) Credito", "4) Pago", "5) Salir"])
        opc4 = menu4.menu()
        if opc4 == "1":
            borrarPantalla()
            print("Clientes")
            mostrarCliente()
            input("Presione cualquier tecla para continuar...\n")
        elif opc4 == "2":
            borrarPantalla()
            print("Factura")
            mostrarFactura()
            input("Presione cualquier tecla para continuar...\n")

        elif opc4 == "3":
            borrarPantalla()
            print("Credito")
            mostrarCredito()
            input("Presione cualquier tecla para continuar...\n")
        elif opc4 == "4":
            borrarPantalla()
            print("Pagos")
            mostrarPago()
            input("Presione cualquier tecla para continuar...\n")
        elif opc4 == "5":
            break
        else:
            input("Opcion invalida\nEscriba cualquier tecla para continuar... ")
    elif opc4 == "6":
        borrarPantalla()
        break
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()
