# Importo las librerias
import os
import shutil

# Configuracion
# Ruta de los archivos
ruta = os.path.join("D:\\", "Serie", "black-clover")
extension = ".mkv"
nomPlantilla = "black-clover"
numCapitulo = 1


# Obtiene los archivos de la ruta
listaArchivos = os.listdir(ruta)

if (len(listaArchivos) == 0):
    print("No hay archivos disponibles.")
    exit()

# Lista de archivos a renombrar o cambiar nombre
listaArchivosRenombrar = []


def ValidarExtension(archivo, extension):
    """Función que permite validar la extension del archivo.

    Parametros:
    -----------
    archivo: String
        Nombre del archivo.

    extension: String
        Extension a validar.

    Retorna:
    Boolean
        True si cumple con la extension y false en caso contrario.
    """
    if (archivo.endswith(extension)):
        return True
    else:
        return False


# Itera cada archivo, valida la extension y lo agrega en la lista de archivos por renombrar
for archivo in listaArchivos:
    if (ValidarExtension(archivo, extension)):
        listaArchivosRenombrar.append(archivo)

# Ordena la lista de archivos a renombrar
listaArchivosRenombrar = sorted(listaArchivosRenombrar, )
# Crea un contador
contador = numCapitulo
# Obtiene la cantidad de digitos de la cantidad de elementos de la lista
canDigitos = len(str(len(listaArchivosRenombrar)))

# Itera la lista de archivos
for archivo in listaArchivosRenombrar:
    # Obtiene el consecutivo
    consecutivo = str(contador)
    # Obtiene la cantidad de digitos del consecutivo
    canDigitoConsecutivo = len(consecutivo)
    # Calcula la diferencia
    diferencia = canDigitos - canDigitoConsecutivo

    # Valida si la diferencia es mayor a cero con el fin de agregar la cantidad de ceros requeridos en el conseutivo
    if (diferencia > 0):
        nuevoConsecutivo = ''
        for i in range(0, diferencia):
            nuevoConsecutivo = nuevoConsecutivo + str("0")
        consecutivo = nuevoConsecutivo + consecutivo

    # Genera la ruta origen y destino
    rutaArchivoOriginal = os.path.join(ruta, archivo)
    rutaArchivoDestino = os.path.join(
        ruta, nomPlantilla + "-" + consecutivo + extension)

    # Actualiza el nombre del archivo
    shutil.copyfile(rutaArchivoOriginal, rutaArchivoDestino)

    # Genera la mensajes
    print(rutaArchivoOriginal)
    print(rutaArchivoDestino)
    print("------------------------")

    # Actualiza el contador
    contador = contador + 1
