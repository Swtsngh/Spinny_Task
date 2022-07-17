from flask import Flask, render_template, url_for, redirect
from flask_sock import Sock
app = Flask(__name__)

sock = Sock(app)
@sock.route('/')
def index():
    return render_template("home.html")

@sock.route("/home")
def home():
    return redirect(url_for('login'))

@sock.route("/login")
def login():
    return render_template("login.html")
