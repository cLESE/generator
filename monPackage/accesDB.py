#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlalchemy

# Connection à la base de données
engine = sqlalchemy.create_engine('postgresql://c.sebillet:passe@172.16.99.2:5432/radio_libre')

# la collection de métadonnées est stockée dans l'objet MetaData
metadonnees = sqlalchemy.MetaData()

# récupère dans table_morceaux la structure de la base de données
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
# s définit la requête à effectuer
s = sqlalchemy.select([table_morceaux])

# défini conn qui établi la connection à la base de données
conn = engine.connect()

# result est la variable qui reçoit la liste des musiques
result = conn.execute(s)