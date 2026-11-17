
import os
from flask import Flask

app = Flask(__name__)

# Lire le message depuis une variable d'environnement
MESSAGE = os.getenv("APP_MESSAGE", "Bienvenue dans mon premier projet Docker !")

@app.route("/")
def home():
    return MESSAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
