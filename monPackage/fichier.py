#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Created on 4 nov. 2014

@author: etudiant
'''
import io
from mercurial.encoding import encoding

    #Si l'extension du fichier est le m3u
def creationFichierm3u(nom, ext, result):
    fichier=io.open(nom + "." + ext,'w')
    #Parcours le résultat pour chaque ligne
    for row in result:
            fichier.write("#EXTINF:" + str(row[5]) + ", " + row[2] + " - " + row[0] + "\n")
            fichier.write(row[8] + "\n\n")
    fichier.close()


    #Si l'extension du fichier est le xspf
def creationFichierxpsf(nom, ext, result):
    fichier=io.open(nom + "." + ext,'w')
    fichier.write(unicode("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"+
                       "<playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n"+
                       "\t<title>"+ nom +"</title>\n"+
                       "\t<trackList>\n"))
    #Parcours le résultat pour chaque ligne
    for row in result:
            fichier.write(unicode("\t\t<track>\n\t\t\t<location>file://"+ row[8] +"</location>\n"+
                               "\t\t\t<title>"+ row[0] +"</title>\n"+
                               "\t\t\t<creator>"+ row[2] +"</creator>\n"+
                               "\t\t\t<album>"+ row[1] +"</album>\n"+
                               "\t\t\t<duration>"+ str(row[5]) +"</duration>\n"+
                               "\t\t</track>\n"))
    fichier.write(unicode("\t</trackList>\n</playlist>"))
    fichier.close()


    #Si l'extension du fichier est le pls
def creationFichierpls(nom, ext, result):
    i=1
    fichier=io.open(nom + "." + ext,'w')
    fichier.write(unicode("[playlist]\n\n"))
    for row in result:
        fichier.write(unicode("File"+ str(i) +"="+ row[8] +"\n"))
        fichier.write(unicode("Title"+ str(i) +"="+ row[0] + "\n"))
        fichier.write(unicode("Length"+ str(i) +"="+ str(row[5]) + "\n\n"))
        i+=1
    fichier.write(unicode("NumberOfEntries="+ str(len(result)) +"\nVersion=2"))
    fichier.close()

    #Si l'extension du fichier est le pls
    #fichier.write("test")

