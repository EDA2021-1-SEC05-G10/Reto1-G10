"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


from prettytable.prettytable import ALL
import config as cf
import controller
import sys
from DISClib.ADT import list as lt
assert cf
from prettytable import PrettyTable

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas que nacieron en un rango de años:")
    print("3- listar cronológicamente las obras adquiridas por el museo en un rango de fechas:")
    print("4- Clasificar las obras de un artista de acuerdo a la técnica utilizada para su creación")
    print("0- Salir")

def initCatalog():
   
    return controller.initCatalog()

def loadData(catalog):
    
    controller.loadData(catalog)

#----------------------

def printreq1(size, final):
    print("Las personas que nacieron en este intervalo de años es: " + str(size))
    print(final)




"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print("La cantidad de artistas en este catalogo es de: " + str(lt.size(catalog["Artists"])))
        print("La cantidad de obras en este catalogo es de: " + str(lt.size(catalog["Artworks"])))
        size = lt.size(catalog["Artists"])
        art = PrettyTable(padding_width=2,hrules = ALL)
        art.field_names = ["Nombre", "Nacimiento", "Fallecimiento", "Nacionalidad","Genero"] 
        idx = 0
        for artist in lt.iterator(catalog["Artists"]):
            if idx >= (size-3):
                lista = [artist["DisplayName"],artist["BeginDate"],artist["EndDate"],artist["Nationality"],artist["Gender"]]
                art.add_row(lista)
                idx += 1
            elif idx < size-3:
                idx += 1
        print(art)

        sizew = lt.size(catalog["Artworks"])
        artw = PrettyTable(borders = True, padding_width=0, hrules = ALL)
        artw.field_names = ["Nombre", "Fecha", "Dimensiones", "Departamento","Adquisición"] 
        artw._max_width={"Nombre":25,"Fecha":6, "Dimensiones":25, "Departamento":14,"Adquisición":10}
        ind = 0
        for artwork in lt.iterator(catalog["Artworks"]):
            if ind >= (sizew-3):
                lista = [artwork["Title"],artwork["Date"],artwork["Dimensions"],artwork["Department"],artwork["DateAcquired"]]
                artw.add_row(lista)
                ind += 1
            elif ind < sizew-3:
                ind += 1
        print(artw)

    elif int(inputs[0]) == 2:
        inicial = input("Año inicial: ")
        final = input("Año final: ")
        size, final = controller.req1(inicial, final, catalog)
        printreq1(size, final)
        
    elif int(inputs[0]) == 3:
        inicial = input("Fecha inicial del intervalo: ")
        final = input("Fecha final: ")
        total, art = controller.req2(inicial, final, catalog)   
        print(total, art)

    elif int(inputs[0]) == 4:
        Name = input("Nombre a buscar: ")
        elm, tabla, tabla2 = controller.req3(catalog,Name)
        print("En el museo hay "+str(elm)+" obras a nombre de "+ Name )
        print("")
        print(tabla)
        print("")
        print(tabla2)

    elif int(inputs[0]) == 5:
   
        Artworks = input("Cantidad de obras: ")
        final = controller.Artworksnacionalidad(catalog, Artworks)

    else:
        sys.exit(0)


