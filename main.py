#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
@author: clément
'''

import logging
from monPackage.pourcentage import gestionPctage
from monPackage.moduleArgparse import fonctionArgparse
logging.basicConfig(filename="monLog.log", level=logging.DEBUG)
logging.info("***** Démarrage du programme *****")

args = fonctionArgparse()

'''Vérifications'''
'''Vérification d'un temps positif'''
logging.info("Utilisation de la fonction pour vérifier que le temps est un entier positif")
if args.temps<0 :
    print ("Le temps doit être positive !")
    logging.error("le temps " + str(args.temps) + " n'est pas un entier positif")
    exit(1)

'''Vérification que les arguments on bien été renseignés'''
for unArg in ['genre','sousgenre','artiste','album', 'titre']:
    '''Si l'argument est renseigné'''
    if getattr(args, unArg) is not None:
        logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
        gestionPctage(getattr(args, unArg))

if (argumentsParser.type_playlist =='m3u'):
    creationFichierm3u(argumentsParser, playlist)
    print('La playlist a bien ete genere')

if(argumentsParser.type_playlist=='xspf'):
    creationFichierxpsf(argumentsParser, playlist)
    print('La playlist a bien ete genere')

if(argumentsParser.type_playlist=='pls'):
    creationFichierpls(argumentsParser, playlist)
    print('La playlist a bien ete genere')

print("Good job team")
logging.info("Tout est bon !!!")
logging.info("***** Fin du programme *****")