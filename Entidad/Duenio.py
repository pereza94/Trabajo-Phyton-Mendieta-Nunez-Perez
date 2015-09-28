# -*- coding: utf-8 -*-
"""
Created  on Wed Sep 16 15:28:33 2015

@author: Alejandro
"""

class Duenio(object):
    
        def __init__(self,dApellido=None,dNombre=None,dDireccion=None,dDNI=None,dTelefono=None):
            self.__dApellido=dApellido
            self.__dNombre=dNombre
            self.__dDireccion=dDireccion
            self.__dDNI=dDNI
            self.__dTelefono=dTelefono
        
        def get_dApellido(self):
            """Devuelve el apellido del dueño"""
            return self.__dApellido
        def get_dNombre(self):
            """Devuelve el nombre del dueño"""
            return self.__dNombre
        def get_dDireccion(self):
            """Devuelve la direccion del dueño"""
            return self.__dDireccion
        def get_dDNI(self):
            """Delvuelve el DNI del dueño"""
            return self.__dDNI
        def get_dTelefono(self):
            """Delvuelve el telefono del dueño"""
            return self.__dTelefono
        def get_dDuenio(self):
            return self.__dApellido,self.__dNombre,self.__dDireccion,self.__dDNI,self.__dTelefono
        
        def set_dApellido(self,nuevoApellido):
            """Modifica el apellido del dueño"""
            self.__dApellido=nuevoApellido
        def set_dNombre(self,nuevoNombre):
            """Modifica el nombre del dueño"""
            self.__dNombre=nuevoNombre
        def set_dDireccion(self,nuevaDireccion):
            """Modifica la direccion del dueño"""
            self.__dDireccion=nuevaDireccion
        def set_dDNI(self,nuevoDni):
            """Modifica el DNI del dueño"""
            self.__dDNI=nuevoDni    
        def set_dTelefono(self,nuevoTelefono):
            """Modifica el telefono del dueño"""
            self.__dTelefono=nuevoTelefono   
        
     
        
       
        
class PruebaDuenio(object):
    import Duenio
    lista_duenio = []
         
    d1=Duenio
    d1.set_dApellido= "Garcia"
    d1.set_dNombre = "Francisco"
    d1.set_dDireccion= "Alvear y Gouchon"
    d1.set_dTelefono= "03447-15432211"
    lista_duenio.append(d1)
        
    d2=Duenio
    d2.set_dApellido= "PiedraBuena"
    d2.set_dNombre = "Roberto"
    d2.set_dDireccion= "J.J Paso 213"
    d2.set_dTelefono= "03447-1543450"
    lista_duenio.append(d2)
        
    '''   d3=Duenio
    d3.__dApellido= "Ciano"
    d3.__dNombre = "Omar"
    d3.__dDireccion= "M. Fernandez 009"
    d3.__dTelefono= "03447-15401256"
    lista_duenio.append(d3)
        
    d4=Duenio
    d4.__dApellido= "Fisio"
    d4.__dNombre = "Eddy"
    d4.__dDireccion= "San Martin 92"
    d4.__dTelefono= "03447-15456788"
    lista_duenio.append(d4)
        
    d5=Duenio
    d5.__dApellido= "Menta"
    d5.__dNombre = "Aitor"
    d5.__dDireccion= "Las Acacias 14"
    d5.__dTelefono= "03447-15455567"
    lista_duenio.append(d5)
    '''
    d=Duenio
    for d in lista_duenio:
       print d.get_dNombre()
      
   