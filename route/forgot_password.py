from flask import Flask, render_template, redirect, Blueprint, request, url_for
from utils.crypt import encriptografar
from utils.db import db

forgot_password = Blueprint('forgot_password', __name__)

@forgot_password.route('/forgot_password', methods = ['GET'])
def gerar_forgot_password():
    return render_template('forgot_password.html')

@forgot_password.route('/forgot_password', methods = ['UPDATE'])
def forgot_password_post():
    username = request.form.get('username')
    password = request.form.get('password').encode('utf-8')
    confirm_password = request.form.get('confirm_password').encode('utf-8')

    print('forgot')
    print(db)
    if password == confirm_password:
        hashed_password = encriptografar(password)
        for i in db:
            if i["username"] == username:
                i['hashed_password'] = hashed_password
                print(i['hashed_password'])

    else:
        return redirect(url_for('gerar_forgot_password'))

    return redirect(url_for('login.gerar_login'))
