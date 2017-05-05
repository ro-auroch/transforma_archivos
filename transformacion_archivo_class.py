"""Script para remplazar buscar, insertar, copiar, modificar cadenas de texto """

import fileinput #genera un stream de caracteres para comparar
import os #manejo de rutas de directorios
import re #manejo de expresiones regulares
from shutil import copy2


class modificar_archivo:

    def __init__(self):
        self.count=0 #numero de archivos encontrados
        self.archivos_modificados=0
        self.lineas_modificadas=0
        #self.lista_archivos=[] #lista de archivos encontrados
    def buscar_archivos_en(self, directorio, extension):
        lista_archivos=[]
        count=0
        extension_lower=extension.lower()
        extension_upper=extension.upper()
        
        for root, dirs, files in os.walk(directorio):
            for file in files:
                if file.endswith(extension_lower)or file.endswith(extension_upper):
                    path=os.path.join(root, file)
                    lista_archivos.append(path)
                    count+=1
                    print(path)
        self.count=count
        return lista_archivos

    #Busca archivos mediante una expresión regular    
    def buscar_archivo_inicia_con(self, comienza_con, directorio, extension):
        lista_archivos=[]
        count=0
        extension_lower=extension.lower()
        extension_upper=extension.upper()
        self.exp_regular=re.compile(comienza_con,re.I)
        
        for root, dirs, files in os.walk(directorio):
            for file in files:
                if (self.exp_regular.search(file)and (file.endswith(extension_lower)or file.endswith(extension_upper))):
                #if (file.startswith(comienza_con)):
                #if (file.endswith(extension_lower)or file.endswith(extension_upper)):
                    path=os.path.join(root, file)
                    lista_archivos.append(path)
                    count+=1
                    print("path", path)
        self.count=count
        return lista_archivos
        

    def get_total_archivos_encontrados(self):
        return self.count

    def get_archivos_modificados(self):
        return self.archivos_modificados

    def get_lineas_modificadas(self):
        return self.lineas_modificadas

    def encontrar_cadena(self, lista_archivos, exp_regular, texto_de_remplazo):
        #print("archivo: ", lista_archivos)
        archivos=0
        lineas=0
        lista_match=[]
        self.exp_regular=re.compile(exp_regular)
        for archivo in lista_archivos:
            #print("for",archivo, end='\n')
            r=archivo
            with fileinput.FileInput(archivo, inplace=0) as archivo: #, backup='.bak'
                for line in archivo:
                    if(self.exp_regular.search(line)):
                        print(r, end='\n')
                        print('se encontro cadena~: ',line, end='\n')
                        cad=r+'~'+line
                        lista_match.append(cad)
                        lineas+=1                        
                    
        self.lineas_modificadas=lineas
        return lista_match

    def encontrar_remplazar_cadena(self, lista_archivos, exp_regular, texto_de_remplazo):
        archivos=0
        lineas=0
        lista_match=[]
        #print("exp regular: ",exp_regular)
        self.exp_regular=re.compile(exp_regular)
        self.exp_sust=re.compile(exp_regular)
        for archivo in lista_archivos:
            r=archivo
            #print(archivo, end='\n')
            with fileinput.FileInput(archivo, inplace=1) as archivo: #, backup='.bak'
                for line in archivo:                    
                    if (print(self.exp_regular.sub(texto_de_remplazo, line), end='')):
                        cad=r+'~'+line
                        lista_match.append(cad)
                        lineas+=1
                        
        self.lineas_modificadas=lineas
        return lista_match

    def encontrar_insertar_linea(self, lista_archivos, cadena_inicio, linea_de_remplazo):
        count=0        
        for archivo in lista_archivos:
            with fileinput.FileInput(archivo, inplace=1, backup='.bak') as archivo:
                for line in archivo:
                    if line.startswith(cadena_inicio):
                        count+=1                        
                    
        self.archivos_modificados=count
        
    def copiar_archivo(self, fuente, destino):
        copy2(fuente, destino)
        

            
            
            

    
