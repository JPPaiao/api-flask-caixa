from flask import Flask
from flask_cors import CORS
from routers.auth.login import login_blueprint
from routers.analise.analise import analise_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_blueprint, url_prefix='/auth')
app.register_blueprint(analise_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
