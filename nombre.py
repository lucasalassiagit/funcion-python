def decirNombre(nombre):
    print(f"Hola {nombre}")
    print("Felicitaciones por haber terminado el curso de Git y GitHub")

def ingNombre():
    nombre = input("Ingrese su nombre: ")
    return nombre

nombre = ingNombre()
decirNombre(nombre)