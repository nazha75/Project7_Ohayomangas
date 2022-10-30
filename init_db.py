# Importer le module os
import os

# Importer la bibliothèque psycopg2
import psycopg2

# Ouvrir une connexion à la base de données project_7 à l'aide de la fonction psycopg2.connect()
conn = psycopg2.connect(
        host= "localhost",
        database= "project_7",
        user= "nazha",
        password= "alahyane")

# Créer un curseur cur à l'aide de la méthode connection.cursor() ce qui permet au code Python d'éxecuter des commandes Postgresql dans une session de base de données
cur = conn.cursor()

# Exécuter la méthode cur.execute(), cela crée une nouvelle table
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 "image text,"
                                 'resume text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Inséré les données dans la table

cur.execute('INSERT INTO books (title, author, image, resume)'
            'VALUES (%s, %s, %s, %s)',
            ('Dr Stone T1',
             'Riichirô Inagaki et Boichi'
             "Taiju, un lycéen tokyoïte, est un jour victime d’un phénomène mystérieux : en une fraction de seconde, l’humanité entière est transformée en pierre ! Des milliers d’années plus tard, à son réveil, il décide de rebâtir la civilisation à partir de zéro avec son ami Senku !! Ne manquez pas ce mélange détonnant de récit de survie et d’aventure S.F. !! Lorsque le scénariste d'Eyeshield 21 et le dessinateur de Sun-ken Rock décident de travailler ensemble, le résultat ne peut être qu'exceptionnel. Issu du prestigieux Weekly Shônen Jump, qui a vu éclore Dragon Ball et One Piece, Dr. Stone séduit d'emblée par son propos novateur et ses enjeux colossaux. Quand le renouveau de l'espèce humaine ne tient qu'à deux garçons, quelles solutions peuvent bien s'offrir à la survie de l'humanité."
             "")
           )


cur.execute('INSERT INTO books (title, author, image, resume)'
            'VALUES (%s, %s, %s, %s)',
            ('Dr Stone T2',
             'Riichirô Inagaki et Boichi'
             "Arrivés dans la région de Hakone, Senku, Taiju et Yuzuriha s’empressent de fabriquer de la poudre à canon. Mais une colonne de fumée s’élève soudain dans le lointain, preuve de l’existence d’autres humains. Senku, conscient des risques que cela implique, décide de répondre à ces signaux de fumée.Tsukasa, qui a pris Senku en chasse, gagne quant à lui du terrain, prêt à tout pour empêcher la fabrication de la poudre.Nos héros se retrouvent alors dans une situation qui paraît sans issue… "
             "")
            )

cur.execute('INSERT INTO books (title, author, image, resume)'
            'VALUES (%s, %s, %s, %s)',
            ('Dr Stone T3',
             'Riichirô Inagaki et Boichi'
             ""
             "")
            )


cur.execute('INSERT INTO books (title, author, image, resume)'
            'VALUES (%s, %s, %s, %s)',
            ('Dr Stone T4',
             'Riichirô Inagaki et Boichi'
             ""
             "")
            )

cur.execute('INSERT INTO books (title, author, image, resume)'
            'VALUES (%s, %s, %s, %s)',
            ('Dr Stone T5',
             'Riichirô Inagaki et Boichi'
             ""
             "")
            )

# Applique les modifications à la base de données
conn.commit()

cur.close()
conn.close()
