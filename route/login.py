from flask import Blueprint,render_template,request,redirect,url_for

login = Blueprint('login', __name__)

@login.route('/', methods = ['GET'])
def gerar_login():
    return render_template('login.html')

@login.route('/', methods = ['POST'])
def login_post():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    return redirect(url_for('index.gerar_index'))