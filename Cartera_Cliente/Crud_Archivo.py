class Archivo:
    def __init__(self, nombrearchivo):
        self.nombrearchivo = nombrearchivo
    def crear_archivo(self, contenido):
        with open("archivos"+self.nombrearchivo + '.txt', 'w') as f:
            f.write(str(contenido))
    def agregar_elemento(self, elemento):
        with open("archivos/"+self.nombrearchivo + ".txt", "a") as archivo:
            archivo.write(elemento + "\n")
    def buscar_elemento(self, elemento):
        with open(f"archivos/{self.nombrearchivo}.txt", 'r') as f:
            for linea in f:
                if elemento in linea:
                    return linea.strip()
        return f"No se encuentra el elemento en la lista"
    def buscar_elemento_lista(self, elemento):
        with open(f"archivos/{self.nombrearchivo}.txt", 'r') as f:
            for linea in f:
                campos = linea.strip().split(",")
                if campos[0] == elemento:
                    return campos
        return f"No se encuentra el elemento en la lista"
    def leer_archivo(self):
        with open(f"archivos/{self.nombrearchivo}.txt", "r") as f:
            return f.readlines()