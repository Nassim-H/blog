import sqlite3

connection = sqlite3.connect('database.db')


with open('donnees/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title,acroche, content, genre) VALUES (?,?,?,?)",
            ('Pourquoi ?',"Pourquoi ais-je mis en place un site dans lequel je liste les films visionnés ? Telle est la question !", "Pour développer ma culture et me souvenir de ma culture....", " hors-catégorie")
            )

cur.execute("INSERT INTO posts (title,acroche, content, genre) VALUES (?,?, ?, ?)",
            ('Pour tous',"A quoi bon créer un site pour soi-même, si ce n'est développer ses compétences en informatique, en rédaction, en graphisme et en culture cinématographique ?", "C'est pas seulement pour moi, pas cette fois ! Je compte vous donner envie de développer votre culture cinématographique, non pas que vous n'en avez pas, mais qu'il y a toujours des films que l'on ne connaît pas. Personne n'a la science infuse."," hors-catégorie")
            )

connection.commit()
