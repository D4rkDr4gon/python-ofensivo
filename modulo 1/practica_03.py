import argparse
import sys
import subprocess  # Importa el módulo subprocess para ejecutar comandos en el sistema operativo

# Llamamos al módulo argparse para manejar los argumentos de línea de comandos
parser = argparse.ArgumentParser()

# Le agregamos un argumento para pasar el dominio
parser.add_argument('-t', '--target', help='indica el URL del sitio web')

# Le pasamos el dominio a parser
args = parser.parse_args()

def main():
    if args.target:  # Verifica si se proporcionó un URL como argumento
        # Ejecuta el comando "wad" para realizar el escaneo de tecnologías y redirige la salida a un archivo "tecnologias.txt"
        subprocess.run("wad -u " + args.target + " > tecnologias.txt", shell=True)

        tecnologias = open("tecnologias.txt", "r")
        tecnologias = tecnologias.read()
        #los separo por sistemas
        tecnologias = tecnologias.split("[")
        tecnologias = tecnologias[1].split("]")
        tecnologias = tecnologias[0].split("{")

        for tecnologia in tecnologias:
            print(tecnologia)
            print("-" * 20)

    else:
        print("(-) Ingresa un URL válido")  # Muestra un mensaje si no se proporciona un URL válido

if __name__ == "__main__":
    try:
        main()  # Llama a la función principal
    except KeyboardInterrupt:
        sys.exit()  # Sale del programa si se presiona Ctrl+C
