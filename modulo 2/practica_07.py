#escaneo de puertos con nmap
import nmap
import sys
import os
import time

def switcher(opcion):
    if(opcion == 1): #escaneo completo
        nmap_cadena = " -p- -A"
        return nmap_cadena
    elif(opcion == 2): #escaneo rapido
        nmap_cadena = " -F"
        return nmap_cadena
    elif(opcion == 3): #escaneo host discovery
        nmap_cadena = " -sn"
        return nmap_cadena
    elif(opcion == 4): #escaneo vulnerabilidades
        nmap_cadena = " -sV --script vuln"
        return nmap_cadena
    elif(opcion == 5): #escaneo OS fingerprint
        nmap_cadena = " -O"
        return nmap_cadena
    elif(opcion == 6): #escaneo versiones
        nmap_cadena = " -sV"
        return nmap_cadena
    else:
        print("Opcion no valida")
        sys.exit()

def parser(modo, consulta, target):
    if modo == 1:
        pass
    elif modo == 2:
        pass
    elif modo == 3:
        pass
    else:
        print ("-" * 50)
        print(target)
        results = os.system(consulta)

def option(opcion, mode, modo):
    if (opcion == 1):
        print("Ingrese la direccion IP a escanear: ")
        target = input("=> ")
        consulta = "nmap " + target + mode
        parser(modo, consulta, target)
        

    else:
        pass



def main():
    print("-------nmap automatizado-------")
    time.sleep(1)

    print("modo de ejecucion:")
    print("[1] Escaneo completo")
    print("[2] Escaneo rapido")
    print("[3] Escaneo host discovery")
    print("[4] Escaneo vulnerailidades")
    print("[5] Escaneo OS fingerprint")
    print("[6] Escaneo versiones")
    print("[#] Salir")

    modo = 1#input("=> ")
    mode = switcher(modo)
    time.sleep(1)
    print("-----------------------------")
    print("opcion: \n [1] IP \n [2] listas de IP" )
    opcion = 1#int(input("=> "))
    option(opcion, mode, modo)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("finalizado...")
        sys.exit()