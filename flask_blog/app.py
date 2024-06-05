from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
 
app = Flask(__name__)

# Required
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flaskblog"
# Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

class RegisterForm(Form):
    name = StringField("İsim Soyisim", validators=[validators.Length(min=4, max=25)])
    username = StringField("Kullanıcı Adı", validators=[validators.Length(min=5, max=35)])
    email = StringField("Email Adresi", validators=[validators.Email(message="Lütfen Geçerli bir e-mail adresi giriniz...")])
    password = PasswordField("Parola", validators= [
        validators.DataRequired(message="Lütfen Parola belirleyin"),
        validators.EqualTo(fieldname= "confirm", message="Parolalar uyuşmamaktadır...")
    ])
    confirm = PasswordField("Parola Doğrula")
   
@app.route("/")
def index():
    articles = [
        {"id" :1, "title" : "Deneme-1", "content": "Deneme içerik 1"},
        {"id" :2, "title" : "Deneme-2", "content": "Deneme içerik 2"},
        {"id" :3, "title" : "Deneme-3", "content": "Deneme içerik 3"},
    ]
    return render_template('index.html', articles = articles)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/article/<string:id>")
def article(id):
    return "Article Id: " + id
 
@app.route("/register")
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)





if __name__ == "__main__":
    app.run(debug=True)

