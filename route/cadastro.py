from flask import Blueprint, render_template, Flask

cadastro = Blueprint('cadastro', __name__)

@cadastro.route('/cadastrar', methods = ['GET'])
def gerar_cadastro():
    return render_template('cadastro.html')