#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 4 nov. 2014

@author: etudiant
'''
import io
from mercurial.encoding import encoding
def creationFichier(nom, ext, result):
    fichier=io.open(nom + "." + ext,'w')
    #Si l'extension du fichier est le m3u
    if ext == "m3u":
        for row in result:
            fichier.write(row[8])
            print(row '')


    #Si l'extension du fichier est le xspf
    fichier.write("test")

    #Si l'extension du fichier est le pls
    fichier.write("test")

    fichier.close()
