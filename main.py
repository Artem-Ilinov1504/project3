from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def add_user():
    username = request.form["username"]
    password = request.form["hashedPassword"]
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return f"{new_user.username}, вы успешно зарегистрировались. Перейдите по ссылке <a>http://127.0.0.1:5000/index</a>"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)