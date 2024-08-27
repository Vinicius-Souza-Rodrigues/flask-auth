from flask import Flask, render_template, redirect, Blueprint, request, url_for, flash
from utils.crypt import encriptografar

forgot_password = Blueprint('forgot_password', __name__)

@forgot_password.route('/forgot_password', methods = ['GET'])
def gerar_fogot_password():
    return render_template('forgot_password.html')

@forgot_password.route('/forgot_password', methods = ['UPDATE'])
def forgot_password_post():
    username = request.form.get('username')
    password = request.form.get('password').encode('utf-8')
    confirm_password = request.form.get('confirm_password').encode('utf-8')

    if password == confirm_password:
        hashed_password = encriptografar(password)
    else:
        #flash('Digite a mesma senha nos campos!')
        return redirect(url_for('gerar_forgot_password'))

    return redirect(url_for('login.gerar_login'))
