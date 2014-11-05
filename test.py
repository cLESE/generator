#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''Fonction de vérification des pourcentages'''

import logging
def verifPourcentage(arg):
    '''
    >>> verifPourcentage(110)
    100
    >>> verifPourcentage(-30)
    30
    >>> verifPourcentage(azr)
    ValueError
    '''
    try:
        pct = int(arg)
        if pct<0:
            pct = abs(pct)
            logging.warning('La quantité saisie doit etre positive')
            logging.info('Nombre négatif transformé en positif: ' + str(pct))
        elif pct>100:
            pct = None
            logging.warning('La quantité saisie est supérieur à 100')
            logging.info('Nombre supérieur à 100 transformé en : ' + str(pct))
    except ValueError:
        logging.error('Impossible de convertir ' + arg + ' en nombre entier !')
        logging.info("***** Fin du programme *****")
exit(1)

print(verifPourcentage(sqf))

import doctest
doctest.testmod()
