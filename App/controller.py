﻿"""
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
 """


import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.initCatalog()
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
   
    loadArtworks(catalog)
    loadArtists(catalog)

def loadArtworks(catalog):
    
    Artworksfile = cf.data_dir + 'Moma/Artworks-small.csv'
    input_file = csv.DictReader(open(Artworksfile, encoding='utf-8'))
    for Artwork in input_file:
        model.addArtworks(catalog, Artwork)

def loadArtists(catalog):
    
    Artistsfile = cf.data_dir + 'Moma/Artists-small.csv'
    input_file = csv.DictReader(open(Artistsfile, encoding='utf-8'))
    for Artists in input_file:
        model.addArtists(catalog, Artists)
    
