from flask import Flask, request
import random

app = Flask(__name__)
db = {}

@app.route('/', methods=['GET'])
def home():
    return '''
          <form method="POST" action="/register">
          <input name="email">
          <input type="submit">
          </form>
          '''

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    code = str(random.random())
    if db_save(email, code):
        html = '<a href="/verify/{email}/{code}">here</a>'.format(email=email, code = code)
        sendmail({'to': email, 'subject': 'Registration', 'html': html })
        return 'OK'
    else:
        return 'FAILED'

@app.route('/verify/<email>/<code>', methods=['GET'])
def verify(email, code):
    if db_verify(email, code):
        sendmail({'to': email, 'subject': 'Welcome!', 'html': '' })
        return 'OK'
    else:
        return 'FAILED'

def sendmail(data):
    pass

def db_save(email, code):
   if email in db:
       return False
   db[email] = code
   return True

def db_verify(email, code):
    return email in db and db[email] == code
