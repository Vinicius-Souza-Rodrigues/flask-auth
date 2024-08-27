from flask import Blueprint,render_template,request,redirect,url_for, flash
import bcrypt
from utils.db import adicionar, db

login = Blueprint('login', __name__)

@login.route('/', methods = ['GET'])
def gerar_login():
    return render_template('login.html')

@login.route('/', methods = ['POST'])
def login_post():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password').encode('utf-8')

    for i in db:
       if i["username"] == username and i["email"] == email and bcrypt.checkpw(password, i["hashed_password"]):
          return redirect(url_for('index.gerar_index'))
    
    #flash('Algo deu errado!')
    return redirect(url_for('login.gerar_login'))