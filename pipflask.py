#pip install flask
from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'Hola amigos de Geeky Theory'

if _name_== '_main_':
    app.run(host='0.0.0.0')