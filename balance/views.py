from flask import jsonify, request, render_template

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
db = DBManager(RUTA)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/v1/movimientos")
def listar_movimientos():
    try:
        
        sql = "SELECT * from movimientos ORDER BY fecha, id"
        movimientos = db.consultaSQL(sql)
        resultado = {"status":"success",
        "results":movimientos}
    except Exception as error:
        resultado = {
        "status":"error",
        "results": str(error)
        }

    return jsonify(resultado)

@app.route("/api/v1/movimientos", methods=["POST"])
def insertar_movimiento():
    try:
        sql = ("INSERT INTO movimientos (fecha, concepto, tipo, cantidad)"
               "VALUES (:fecha, :concepto, :tipo, :cantidad)")
        check = db.consulta_con_parametros(sql, request.json)
        if check:
            resultado = {
                "status":"success"
            }
        else:
            resultado = {
                "status":"error",
                "message":"Error al insertar movimiendo en DB"
            }
    except Exception as error:
        resultado = {
            "status:": "error",
            "message" : str(error)
            
        }
    return jsonify(resultado)

@app.route("/api/v1/movimientos/<int:id>", methods=["DELETE"])
def borrar_movimiento(id):
    try:
        sql = "DELETE FROM movimientos WHERE id=?"
        params = (id,)
        check = db.consulta_con_parametros(sql, params)
        if check:
            status_code = 204
            resultado = {
                "status":"success"
            }
            return resultado, status_code
        else:
            status_code = 500
            resultado = {
                "status":"error",
                "error":"No se pudo borrar el movimiento"
            }
    except Exception as error:
        resultado = {
            "status":"error",
            "error":str(error)
        }
        return resultado, status_code
    

@app.route("/api/v1/movimientos/<int:id>", methods=["POST"])
def sobreescribe_movimiento(id):
    try:
        sql = ("UPDATE movimientos SET (fecha, concepto, tipo, cantidad) WHERE id=?" 
                "VALUES(:fecha, :concepto, :tipo, :cantidad)")
        params = []

        diccionario = request.json
        for elem in diccionario:
            params.append(diccionario[elem])
        params.pop(0)
        params = tuple(params)
        print(params)

        db = DBManager(RUTA)
        check = db.consulta_con_parametros(sql, params)
        if check:
            resultado={
                "status":"success"
            }
        else:
            resultado={
                "status":"error",
                "error":"No se pudo sobreescribir el movimiento"
            }
    except Exception as error:
        resultado={
            "status":"error",
            "error": str(error)
        }
    return resultado
        
@app.route("/api/v1/movimientos/<int:id>")
def obtener_movimiento_por_id(id):
    movimiento = db.obtener_movimiento_por_id(id)
    if movimiento:
        resultado = {
            "status":"success",
            "results":movimiento
        }
        status_code=200
    else:
        resultado = {
            "status":"error",
            "error": f"No he encontrado el movimiento con id {id}"
        }
        
    return jsonify(resultado), status_code