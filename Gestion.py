import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="votre_nom_utilisateur",
  password="votre_mot_de_passe"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE boutique")

mydb = mysql.connector.connect(
  host="localhost",
  user="votre_nom_utilisateur",
  password="votre_mot_de_passe",
  database="boutique"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE categorie (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255))")

mycursor.execute("CREATE TABLE produit (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), description TEXT, prix INT, quantite INT, id_categorie INT, FOREIGN KEY (id_categorie) REFERENCES categorie(id))")

sql = "INSERT INTO categorie (nom) VALUES (%s)"
val = [
  ('Informatique'),
  ('Electronique'),
  ('Maison'),
  ('Jardin')
]

mycursor.executemany(sql, val)
mydb.commit()

sql = "INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)"
val = [
  ('Ordinateur portable', 'PC portable HP', 800, 10, 1),
  ('Téléviseur', 'TV Samsung 55 pouces', 1000, 5, 2),
  ('Canapé', 'Canapé en cuir', 600, 3, 3),
  ('Tondeuse', 'Tondeuse à gazon électrique', 200, 8, 4)
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "produits insérés.")
