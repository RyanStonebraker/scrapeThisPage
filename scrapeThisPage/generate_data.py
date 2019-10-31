import random
import os
import requests
import pymysql

with open("cat_names.txt", "r") as cat_reader:
    cat_names = [name.strip() for name in cat_reader.readlines()]

random_sentence = requests.get("https://randomwordgenerator.com/json/sentences.json").json()["data"]

pictures = os.listdir(os.path.join(os.path.dirname(__file__), "upload"))

cats = []
for picture in pictures:
    cat = {}
    cat["picture"] = "/upload/{}".format(picture)
    cat["name"] = random.choice(cat_names)
    cat["price"] = random.randrange(0, 1000000)
    cat["description"] = random.choice(random_sentence)["sentence"]
    cats.append(cat)


conn = pymysql.connect(host="localhost", user="root", password="", db="catdb", use_unicode=True, charset='utf8')
cursor = conn.cursor()
cursor.execute("TRUNCATE cats")
for cat in cats:
    query = """
        INSERT INTO cats (name, price, description, picture)
        VALUES ("{catName}", {catPrice}, "{catDescription}", "{catPicture}")
    """.format(catName=cat["name"], catPrice=cat["price"], catDescription=cat["description"], catPicture=cat["picture"])
    cursor.execute(query)
    conn.commit()
