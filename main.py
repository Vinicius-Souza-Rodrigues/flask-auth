from flask import Flask, render_template
from route.cadastro import cadastro
from route.login import login, gerar_login
from route.index import index
app = Flask(__name__)

#registrar blueprint
app.register_blueprint(login)
app.register_blueprint(cadastro)
app.register_blueprint(index)


if __name__ == '__main__':
    app.run(debug=True)