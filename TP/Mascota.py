# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:07:56 2015

@author: Alejandro
"""

class Mascotas(object):
    def __init__(self,MNombre=None,MRaza=None,MPeso=None,MCodMascota=None):
        self.__MNombre=MNombre
        self.__MRaza=MRaza
        self.__MPeso=MPeso
        self.__MCodMascota=MCodMascota
        
        
        def get_MNombre(self):
            """Devuelve el nombre de una mascota"""
            return self.__MNombre
        def get_MRaza(self):
            """Devuelve la raza de una Mascota"""
            return self.__MRaza
        def get_MPeso(self):
            """Devuelve el peso de una mascota"""
            return self.__MPeso         
        def get_MCodMascota(self):
            """Devuelve el codigo de una mascota"""
            return self.__MCodMascota
        
        def set_MNombre(self,nom):
            """Modifica el nombre de una MAscota"""
            self.__MNombre=nom
        def set__MRaza(self,nraza):
            """Modifica la raza de una mascota"""
            self.__MRaza=nraza
        def set_MPeso(self,npeso):
            """Modifica el peso de una mascota"""
            self.__MPeso=npeso
        def set_MCodMascota(self,nCodMascota):
            """Modifica el codigo de una mascota"""
            self.__MCodMascota=nCodMascota
 

            
            
        
        
    
    