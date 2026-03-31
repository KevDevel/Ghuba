from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Game

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your_secret_key"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    cards = Game.query.all()
    return render_template("index.html", cards=cards)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)