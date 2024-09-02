from flask import Flask, render_template
from route.cadastro import cadastro
from route.login import login
from route.index import index
from route.forgot_password import forgot_password

app = Flask(__name__)

app.secret_key = 'SJDWQNMDIQWBNIUYXBWEIUDBQWCBQIU'

app.register_blueprint(login)
app.register_blueprint(cadastro)
app.register_blueprint(index)
app.register_blueprint(forgot_password)

if __name__ == '__main__':
    app.run(debug=True)