from flask import Flask, request, render_template, abort, redirect, url_for
import pymongo
import datetime

app = Flask(__name__)

config = {
    "username": "root",
    "password": "Secret",
    "server": "mongo",
}

connector = "mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
client = pymongo.MongoClient(connector)
db = client["demo"]

@app.route("/")
def main():
    return render_template('main.html')


@app.route("/save", methods=['POST'])
def save():
    entry = {
        "name": request.form['name'],
        "email": request.form['email'],
        "id": request.form['idnum'],
        "when": datetime.datetime.now(),
    }
    res = db.people.insert(entry)
    db.people.create_index("id", unique=True)
    return render_template('main.html')

@app.route("/list", methods=['GET'])
def list_people():
    count = db.people.count_documents({})
    people = db.people.find({})
    return render_template('list.html', count=count, people=people)

@app.route("/person/<idnum>", methods=['GET'])
def person(idnum):
    person = db.people.find_one({ 'id': idnum })
    if not person:
        abort(404)
    return render_template('person.html', person=person)


@app.errorhandler(404)
def not_found(error):
    app.logger.info(error)
    return render_template('404.html'), 404

@app.route("/get", methods=['POST'])
def get():
    name = request.form['name']
    doc = db.people.find_one({'name' : {'$regex': name}})
    if doc:
        app.logger.info(doc)
        return redirect(url_for('person', idnum=doc["id"]) )
    return render_template('main.html', error="Could not find that person")
