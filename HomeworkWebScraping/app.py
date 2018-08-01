from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["database"]

collection = db["mars"]

@app.route("/")
def home():
    data = collection.find_one()

    return render_template("index.html", data=data)

@app.route("/scrape")
def scrape():
    scrape_update = scrape_mars.scrape()

    collection.insert_one(scrape_update)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)