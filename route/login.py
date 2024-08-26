from flask import Blueprint,render_template,request,redirect,url_for
from utils.crypt import encriptografar
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
    hashed_password = encriptografar(password)

    print(username, email, hashed_password)

    for i in db:
       if i["username"] == username and i["hashed_password"] == hashed_password:
          print('tudo cerot')
          return redirect(url_for('index.gerar_index'))

    return redirect(url_for('login.gerar_login'))