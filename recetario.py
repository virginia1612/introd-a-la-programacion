import json
class Receta:
    def __init__(self, nombre, ingredientes, pasos,t_preparacion,t_coccion,f_creacion):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pasos = pasos
        self.t_preparacion = t_preparacion
        self.t_coccion = t_coccion
        self.f_creacion = f_creacion

    

    def guardar(self):
        # Cargamos la lista de recetas desde el archivo JSON
        with open("recetas.json", "r") as archivo:
            recetas = json.load(archivo)
            # Buscamos si la receta ya existe en la lista de recetas
        for i, receta in enumerate(recetas):
            if receta["nombre"] == self.nombre:
                    # Si la receta ya existe, la actualizamos en la lista de recetas
                recetas[i] = {
                    "nombre": self.nombre,
                    "ingredientes": self.ingredientes,
                    "pasos": self.pasos
                }
                break
            else:
                # Si la receta no existe, la añadimos a la lista de recetas
                recetas.append({
                    "nombre": self.nombre,
                    "ingredientes": self.ingredientes,
                    "pasos": self.pasos
                })

            # Guardamos la lista de recetas actualizada en el archivo JSON
            with open("recetas.json", "w") as archivo:
                json.dump(recetas, archivo, indent=4)

    @staticmethod
    def obtener_recetas():
        # Cargamos la lista de recetas desde el archivo JSON
        with open("recetas.json", "r") as archivo:
            recetas = json.load(archivo)

        # Creamos una lista de objetos Receta a partir de la lista de recetas cargada desde el archivo JSON
        lista_recetas = []
        for receta in recetas:
            lista_recetas.append(Receta(receta["nombre"], receta["ingredientes"], receta["pasos"], receta["t_preparacion"], receta["t_coccion"], receta["f_creacion"]))

        return lista_recetas

    @staticmethod
    def obtener_receta(nombre):
        # Cargamos la lista de recetas desde el archivo JSON
        with open("recetas.json", "r") as archivo:
            recetas = json.load(archivo)

        # Buscamos la receta con el nombre especificado y la devolvemos como objeto Receta
        for receta in recetas:
            if receta["nombre"] == nombre:
                return Receta(receta["nombre"], receta["ingredientes"], receta["pasos"], receta["t_preparacion"], receta["t_coccion"], receta["f_creacion"])

        # Si no se encontró ninguna receta con el nombre especificado, devolvemos None
        return None

    @staticmethod
    def eliminar_receta(nombre):
        # Cargamos la lista de recetas desde el archivo JSON
        with open("recetas.json", "r") as archivo:
            recetas = json.load(archivo)

        # Buscamos la receta con el nombre especificado y la eliminamos de la lista de recetas
        for i, receta in enumerate(recetas):
            if receta["nombre"] == nombre:
                del recetas[i]
                break

        # Guardamos la lista de recetas actualizada en el archivo JSON
        with open("recetas.json", "w") as archivo:
            json.dump(recetas, archivo, indent=4)
            
            
    def __str__(self):
        return f"nombre: {self.nombre}, ingredientes:  {self.ingredientes}, pasos: {self.pasos}, t_preparacion: {self.t_preparacion}, t_coccion: {self.t_coccion}, f_creacion: {self.f_creacion}"

pizza = Receta("Pizza", "Masa, queso y tomate", "cocer", "10 min", "5 min", "050323")
print(pizza)
