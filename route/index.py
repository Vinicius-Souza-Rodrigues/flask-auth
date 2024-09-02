from flask import Flask, redirect, render_template, Blueprint, session, url_for
from utils.db import db

index = Blueprint('index', __name__)

@index.route('/main', methods = ['GET'])
def gerar_index():
    token = session.get('token')
    user_id = session.get('user_id')

    if not token and user_id:
        return redirect(url_for('login.gerar_login'))
    
    for user in db:
        if user["account_info"]["user_id"] == user_id:
            user_info = user
            break

    return render_template('index.html', user_info=user_info)

@index.route('/logout', methods = ['GET'])
def logout_user():
    print('a')
    session.clear()
    print('ab')
    return redirect(url_for('login.gerar_login'))