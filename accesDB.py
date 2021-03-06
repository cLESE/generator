#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sqlalchemy
from monPackage.fichier import creationFichierxpsf
from monPackage.fichier import creationFichierm3u
from monPackage.fichier import creationFichierpls

engine = sqlalchemy.create_engine('postgresql://c.sebillet:passe@172.16.99.2:5432/radio_libre')

metadonnees = sqlalchemy.MetaData()

table_morceaux = sqlalchemy.Table('morceaux',metadonnees,
                                  sqlalchemy.Column('titre',sqlalchemy.String),
                                  sqlalchemy.Column('album',sqlalchemy.String),
                                  sqlalchemy.Column('artiste',sqlalchemy.String),
                                  sqlalchemy.Column('genre',sqlalchemy.String),
                                  sqlalchemy.Column('sousgenre',sqlalchemy.String),
                                  sqlalchemy.Column('duree', sqlalchemy.Integer),
                                  sqlalchemy.Column('format',sqlalchemy.String),
                                  sqlalchemy.Column('polyphonie',sqlalchemy.Integer),
                                  sqlalchemy.Column('chemin',sqlalchemy.String)
                                  )

s = sqlalchemy.select([table_morceaux])

conn = engine.connect()
result = conn.execute(s)

'''for row in result:
    print(row)'''


#creationFichierxpsf("testxpsf", "xpsf", result)
#creationFichierm3u("testm3u", "m3u", result)
#creationFichierpls("testpls", "pls", result)