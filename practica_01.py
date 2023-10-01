#analisis de subdominios
import sys
import requests  # Para realizar solicitudes HTTP
from os import path
import argparse  # Para manejar argumentos de línea de comandos
import re  # Para usar expresiones regulares

# Llamamos al módulo argparse para manejar los argumentos de línea de comandos
parser = argparse.ArgumentParser()

# Le agregamos un argumento para pasar el dominio
parser.add_argument('-t', '--target', help='Indicar el dominio')

# Le pasamos el dominio a parser
args = parser.parse_args()

def main():
    if args.target:
        if path.exists('subdominios.txt'): #constatamos los dominios de url comparandolos con la de subdominios de nuestro diccionario
            wordlist = open('subdominios.txt', 'r')
            wordlist = wordlist.read().split('\n')
            
            # Para dominios http
            for subdominio in wordlist:
                # Construye la URL
                url = f"http://{subdominio}.{args.target}"
                
                # Verifica si la URL es válida antes de hacer la solicitud HTTP
                if is_valid_url(url):
                    try:
                        requests.get(url)  # Realiza una solicitud HTTP a la URL
                        print("(+) subdominio encontrado: " + url)
                    except requests.ConnectionError:
                        pass

            # Para dominios https
            for subdominio in wordlist:
                # Construye la URL
                url = f"https://{subdominio}.{args.target}"
                
                # Verifica si la URL es válida antes de hacer la solicitud HTTP
                if is_valid_url(url):
                    try:
                        requests.get(url)  # Realiza una solicitud HTTP a la URL
                        print("(+) subdominio encontrado: " + url)
                    except requests.ConnectionError:
                        pass
        
    else:
        print("(-) ingresa un target")

# Función para verificar si una URL tiene el formato correcto utilizando expresiones regulares
def is_valid_url(url):
    url_pattern = re.compile(r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}(/.*)?$')
    return bool(url_pattern.match(url))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
