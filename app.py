from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)

db.create_all()

@app.route('/', methods=["GET","POST"])
def home():
    if request.form:
        person = Register(name=request.form.get("name"))
        db.session.add(person)
        db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees)

@app.route("/update", methods=["POST"])
def update():
    person = Register.query.filter_by(name=request.form.get("oldname")).first()
    person.name = request.form.get("newname")
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    person = Register.query.filter_by(name=request.form.get("name")).first()
    db.session.delete(person)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
