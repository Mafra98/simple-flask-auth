from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///database.db'
db = SQLAlchemy(app)

@app.route("/hello-word",methods=["GET"])
def hello_word():
    return "Hello Word"

if __name__ == "__main__":
    app.run(debug=True)