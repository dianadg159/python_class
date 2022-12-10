from Bio import Entrez
import argparse

# Pedir la informacion a buscar
parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-t", "--termino",
                    help="Organismo y genes a asociar sin espacios. ej:'Organismo1:gene1,gene2; Organismo2:gene3,gene4'",
                    type=str,
                    required=True)
info = parser.parse_args()

Entrez.email = "diana.delgado.gtz@gmail.com"
# Para un query


def crear_termino(info):
    # Lista donde estara el query
    list = []
    # Recorremos la lista para buscar los organismos
    for organismo in info.split(";"):
        # Editar organismo
        organismo = organismo.split(":")
        # agregar el organismo
        termino = organismo[0] + "[Orgn] AND ("
        # Empezar un contador
        i = 1
        # Recorrer los genes
        for gen in organismo[1].split(","):
            # Si solo es un gen
            if i == len(organismo[1].split(",")):
                gen = gen + "[Gene])"
            # Si hay más de un gen
            else:
                gen = gen + "[Gene] OR "
                i = i + 1
            # juntar el organismo con sus genes
            termino = termino + gen
        # Guardar el primer organismo
        list.append(termino)
    return(list)


def buscar_db(termino):
    # buscamos en la base de datos
    record = Entrez.read(Entrez.egquery(term=termino))
    # Inicializamos un diccionario donde estaran los ids
    # de la base de datos
    idsdb = {}
    # recorrer las bases de datos y sus conteos
    for db in record["eGQueryResult"]:
        # quitar los match que tienen error o 0
        if db["Count"] != "Error" or db["Count"] != "0":
            DbName = db["DbName"]
        # acceder a la lista de ids
        IdList = Entrez.read(Entrez.esearch(db=DbName, term=termino))["IdList"]
        idsdb[DbName] = IdList
    return(idsdb)


terminos = crear_termino(info.termino)
buscar_db(terminos[0])
