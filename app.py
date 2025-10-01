from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hola, mundo desde Flask con GitHub Actions!"}

@app.route("/secret")
def secret():
    secret_value = os.getenv("MY_SECRET", "No se encontró el secret")
    return {"secret": secret_value}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
