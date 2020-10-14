from flask import Flask, request, render_template
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
    field = request.form['field']
    value = request.form['value']
    entry = {
        "field": field,
        "value": value,
        "when": datetime.datetime.now(),
    }
    res = db.people.insert(entry)
    doc = db.people.find_one({'field' : field})
    app.logger.debug(doc)
    doc = db.people.find_one({'field' : field})
    new_value = doc["value"]
    return render_template('main.html', saved=1, value=new_value)

@app.route("/get", methods=['POST'])
def get():
    field = request.form['field']
    doc = db.people.find_one({'field' : field})
    if doc is None:
        return render_template('main.html', field=field, value="Not defined yet")
    str_value = doc["value"]
    return render_template('main.html', field=field, value=str_value)
