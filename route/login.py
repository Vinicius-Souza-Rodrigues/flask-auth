from flask import Blueprint,render_template,request,redirect,url_for, session
import bcrypt
import secrets
from utils.db import adicionar, db

login = Blueprint('login', __name__)

@login.route('/', methods = ['GET'])
def gerar_login():
    return render_template('login.html')

@login.route('/', methods = ['POST'])
def login_post():
    try:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password').encode('utf-8')

        for i in db:
            if i["username"] == username and i["email"] == email and bcrypt.checkpw(password, i["hashed_password"]):
                token = secrets.token_hex(24)
                session["token"] = token
                session["user_id"] = i["account_info"]["user_id"]

                return redirect(url_for('index.gerar_index'))
    
    except Exception as ex:
        #flash('Algo deu errado!')
        print(ex)

    return redirect(url_for('login.gerar_login'))