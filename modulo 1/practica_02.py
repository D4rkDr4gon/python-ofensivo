#bannergrabing
import socket  # Importa el módulo de socket para la comunicación
import sys

def banner(ip, port):  # Función para obtener el banner
    s = socket.socket()  # Crea un objeto de socket
    s.connect((ip, port))  # Establece una conexión a la IP y puerto proporcionados
    print(str(s.recv(1024)))  # Recibe datos del servidor y los imprime en la consola

def main():
    ip = input("Ingresa una dirección IP: ")  # Solicita al usuario una dirección IP
    port = int(input("Ingresa un puerto abierto: "))  # Solicita al usuario un puerto abierto

    banner(ip, port)  # Llama a la función banner con la IP y puerto proporcionados

if __name__ == "__main__":
    try:
        main()  # Llama a la función principal
    except KeyboardInterrupt():  # Captura una excepción si se presiona Ctrl+C
        sys.exit()  # Sale del programa si se presiona Ctrl+C
