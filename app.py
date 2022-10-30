from flask import Flask
import os
import psycopg2
# L'objet request globale permet d'accéder aux données soumises dans un formulaire
# La fonction url_for() génère des liens
# La fonction redirect() redirige les utilisateurs vers des pages du site
from flask import Flask, render_template,request, url_for, redirect

app = Flask(__name__)

# Définir une fonction get_db_connection(), qui ouvre une connexion à la base de données project_7
def get_db_connection():
    conn = psycopg2.connect(host= "localhost",
                            database="project_7",
                            user= 'nazha',
                            password= 'alahyane',)
    return conn

# Créer une route et une fonction index à l'aide de app.route()
@app.route('/')
def index():
# Ouvrir la connection à la base de données
    conn = get_db_connection()
    cur = conn.cursor()
# Créer un curseur et exécuter l'instruction SQL SELECT*FROM pour obtenir tous les livres qui se trouvent dans la base de données
    cur.execute('SELECT * FROM books;')
# Utiliser la méthode fetchall pour enregistrer les données dans une variable books
    books = cur.fetchall()
# Fermer le curseur et la connection
    cur.close()
    conn.close()
# Renvoyez un appel à la fonction render_template() pour afficher le fichier index.html en lui transmettant la liste des livres qu'on a extrait de la base de données dans la variable books
    return render_template('index.html', books=books)

# Dans cette route on passe le tuple ('GET', 'POST') au paramètre method pour autoriser les requêtes GET et POST
# Les requêtes GET sont utilisées pour récupérer les données du serveur
# Les requêtes POST sont utilisées pour publier des données sur une route spécifique
@app.route('/create/', methods=('GET', 'POST'))
def create():
# Gérer les requêtes POST dans la condition if request.method == 'POST' et extraire le titre, l'auteur, l'image et le résumé soumis par l'utilisateur à partir de l'objet request.form
    if request.method == 'POST':
        title = request.form['title']
        author= request.form['author']
        image= request.form['image']
        resume= request.form['resume']
        
        conn = get_db_connection()
        cur = conn.cursor()
# Exécuter une instruction INSERT INTO SQL pour insérer le titre, l'auteur, l'image et le résumé
        cur.execute('INSERT INTO books (title, author, image, resume)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, image, resume))
        conn.commit()
        cur.close()
        conn.close()
# Rediriger l'utilisateur vers la page index ou il peut voir le livre qui viens d'être ajouté sous les livres déjà existants
        return redirect(url_for('index'))
    return render_template('create.html')

# Renvoie vers le fichier 404.html chaque fois que l'utilisateur ouvre un lien qui n'existe pas
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404






