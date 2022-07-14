from flask import Flask

app = Flask(__name__)
app.config.from_object("config") #Busca un archivo config.py para ponerlo como configuracion de Flask