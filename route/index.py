from flask import Flask, redirect, render_template, Blueprint

index = Blueprint('index', __name__)

@index.route('/main', methods = ['GET'])
def gerar_index():
    return render_template('index.html')
