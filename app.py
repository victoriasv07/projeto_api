from flask import Flask, render_template
from random_data import pessoas
import  funcoes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

from api import bp
app.register_blueprint(bp)

if __name__ == 'main':
    app.run(host="0.0.0.0")