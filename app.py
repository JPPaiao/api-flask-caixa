from flask import Flask
from flask_cors import CORS
from routers.auth.login import login_blueprint
from routers.analise.routers_table_month import analise_blueprint
from routers.analise.analise_excel import analise_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_blueprint, url_prefix='/')
app.register_blueprint(analise_blueprint, url_prefix='/analysis/')

if __name__ == '__main__':
    app.run(debug=True)
