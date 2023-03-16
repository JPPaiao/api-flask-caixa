from flask import Flask
from routers.auth.login import login_blueprint
from routers.analise.analise import analise_blueprint

app = Flask(__name__)

app.register_blueprint(login_blueprint, url_prefix='/auth')
app.register_blueprint(analise_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
