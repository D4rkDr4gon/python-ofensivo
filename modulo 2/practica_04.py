#Escaneo de puertos con socket
import socket
import sys
from datetime import datetime

def main():
    target = input("Ingrese la dirección IP a escanear: ")
    port_range = input("Ingrese el rango de puertos a escanear (ejemplo 5-100): ")
    
    print("-" * 50)
    print("Escaneando el objetivo: " + target)
    print("Tiempo iniciado: " + str(datetime.now()))
    print("-" * 50)

    for port in range(int(port_range.split('-')[0]), int(port_range.split('-')[1])):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target, port))
        if result == 0:
            print("[+] El puerto {} está abierto".format(port))
        s.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()