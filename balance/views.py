from flask import jsonify

from . import app
from .models import DBManager

'''
GET /movimientos        DEVUELVE una lista de movimientos
POST  /movimientos      CREA un movimiento
GET /movimientos/1      LEER movimiento con id 1
POST /movimientos/1     ACTUALIZA wl movimiento con id 1 sobreescribiendo el objeto completo
PUT /movimientos/1      ACTUALIZA el movimiento con id 1 sobreescribiendo parcialmente
DELETE /movimientos/1   ELIMINA el movimiento con id 1

importante versionar los endpoints
/api/version/...
'''
RUTA = app.config.get("RUTA")
@app.route("/api/v1/movimientos")
def listar_movimientos():
    db = DBManager(RUTA)
    sql = "SELECT * from movimientos ORDER BY fecha, id"
    movimientos = db.consultaSQL(sql)

    return jsonify(movimientos)