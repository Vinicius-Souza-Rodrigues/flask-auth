from flask import Blueprint, render_template, Flask, redirect, request, url_for
from utils.crypt import encriptografar
from utils.db import db, adicionar

cadastro = Blueprint('cadastro', __name__)

@cadastro.route('/cadastrar', methods = ['GET'])
def gerar_cadastro():
    return render_template('cadastrar.html')

@cadastro.route('/cadastrar', methods = ['POST'])
def cadastro_post():
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password').encode('utf-8')
    confirm_password = request.form.get('confirm_password').encode('utf-8')    
    
    if password == confirm_password:
        hashed_password = encriptografar(password)
    else:
        #flash('Valores errados!')
        return redirect(url_for('cadastro.gerar_cadastro'))
    
    adicionar(name, username, email, hashed_password)
    #flash("usuario cadastrado")

    return redirect(url_for('login.gerar_login'))
