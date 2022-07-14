from . import app

@app.route("/")
def inicio():
    return f"Confugracion actual {app.config['SECRET_KEY']}"