"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


#from App.view import Artists



import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from prettytable import PrettyTable
from prettytable import ALL
import datetime as dt
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def initCatalog():
    
    catalog = {'Artists': None,
               'Artworks': None,
               }

    catalog['Artists'] = lt.newList()
    catalog['Artworks'] = lt.newList('ARRAY_LIST',
                                    )

    return catalog

def addArtworks(catalog, Artwork):

    lt.addLast(catalog['Artworks'], Artwork)
    
    
def addArtists(catalog, Artists):
    
    lt.addLast(catalog['Artists'], Artists)

#Funciones de comparacion
def compareBegin(autor1,autor2):
    return (autor1['BeginDate'] < autor2['BeginDate'])

def compareDate(art1,art2):
    if art1['DateAcquired'] != "" and art2['DateAcquired']!="":
        art1 = art1['DateAcquired'].split("-")
        art2 = art2['DateAcquired'].split("-")
        return (dt.datetime(int(art1[0]),int(art1[1]),int(art1[2])) < dt.datetime(int(art2[0]),int(art2[1]),int(art2[2])))

def sortBegin(catalog):
    sorted_list = sa.sort(catalog, compareBegin)
    return sorted_list

def sortDate(catalog):
    sorted_list = sa.sort(catalog, compareDate)
    return sorted_list

#Funciones del reto:


#Requerimiento 1: artistas por año ------------------------------------------------------------
def requ1(inicial, final, catalog): 
    catalog["Artists"] = sortBegin(catalog["Artists"]) 
    a = PrettyTable(hrules = ALL)
    a.field_names = ["Nombre", "Nacimiento", "Fallecimiento", "Nacionalidad","Genero"]  
    a._max_width={"Nombre":25,"Nacimiento":14,"Fallecimiento":14, "Nacionalidad":17, "Genero":17}  
    lista = lt.newList()
    for artist in lt.iterator(catalog["Artists"]):
        if artist["BeginDate"]>=str(inicial) and artist["BeginDate"]<=str(final) :
            x= [artist["DisplayName"],artist["BeginDate"],artist["EndDate"],artist["Nationality"],artist["Gender"]]
            a.add_row(x)
            lt.addLast(lista,x)
    sizem = lt.size(lista)
    sizex = sizem
    idx = 3
    if sizex > 6:
        while idx >= 3:
            if sizex == 6:
                break
            a.del_row(idx)
            sizex -= 1
    return sizem, a


#Requerimiento 2: obras por intervalo de compra---------------------------------------------
def requ2(inicial,final,catalog):
    catalog["Artworks"] = sortDate(catalog["Artworks"])
    def divFechas(fecha):
        fecha = fecha.split("-")
        return fecha 
    inicial = divFechas(inicial)
    final = divFechas(final)
    art = PrettyTable(hrules = ALL)
    art.field_names = ["Titulo", "Año", "Medio", "Dimesiones","Fecha de compra"]
    art._max_width={"Titulo":17,"Año":14,"Medio":15, "Dimensiones":17, "Fecha de compra":14} 
    lista = []
    idx = 6
    for artw in lt.iterator(catalog["Artworks"]):
        if artw["DateAcquired"] != "":
            fecha = divFechas(artw["DateAcquired"])
            if dt.datetime(int(inicial[0]),int(inicial[1]),int(inicial[2]))<=dt.datetime(int(fecha[0]),int(fecha[1]),int(fecha[2])):
                if dt.datetime(int(fecha[0]),int(fecha[1]),int(fecha[2])) <= dt.datetime(int(final[0]),int(final[1]),int(final[2])):
                    lista.append([artw["Title"],artw["Date"],artw["Medium"],artw["Dimensions"],artw["DateAcquired"]])
    sizem = len(lista)
    for cada in lista:
        if lista.index(cada)>= 0 and lista.index(cada)<3:
            art.add_row(cada)
        if lista.index(cada)>= sizem-3 and lista.index(cada)< sizem:
            art.add_row(cada)
    total = "El total de obras en este rango es de: " + str(sizem) + "\n"
    return total, art

#Requerimiento 3:      -------------------------------------------------------
def requ3(catalog, Name):
    lista = []
    medios = {}
    listamedios=[]
    for artista in lt.iterator(catalog["Artists"]):
        if artista["DisplayName"] == Name:
            id = artista["ConstituentID"]
            for obras in lt.iterator(catalog["Artworks"]):
                id2 = obras["ConstituentID"].replace("[","").replace("]","").replace(" ","").split(",")
                if len(id2) == 1:
                    if id == id2[0]:
                        lista.append([obras["Title"],obras["Date"],obras["Medium"],obras["Dimensions"]])
                        listamedios.append(obras["Medium"])
                        medios[obras["Medium"]] = 1
                elif len(id2) > 2:
                    if id in id2:
                        lista.append([obras["Title"],obras["Date"],obras["Medium"],obras["Dimensions"]])
                        listamedios.append(obras["Medium"])
                        medios[obras["Medium"]] = 1
    listamedios = dict((i, listamedios.count(i)) for i in listamedios)
    mayor = ""
    may = 0
    for can in listamedios.values():
        if can > may:
            may = can
    for obr, can in listamedios.items():
        if mayor == "": 
            if can == may:
                mayor=[obr,may]
    mediosT = PrettyTable(hrules = ALL)
    mediosT.field_names = ["Medio","Cantidad"] 
    for med, cant in listamedios.items():
        lis = [med,cant]
        mediosT.add_row(lis)
    mediosFinal = mediosT.get_string(sortby="Cantidad")
    tabla2 = PrettyTable(hrules = ALL)
    tabla2.field_names = ["Titulo","Año","Medio","Dimensiones"]
    tabla2._max_width={"Titulo":25,"Año":14, "Dimensiones":30}
    for obras in lista:
        if obras[2] == mayor[0]:
            tabla2.add_row(obras)
    return len(lista), mediosFinal,tabla2

