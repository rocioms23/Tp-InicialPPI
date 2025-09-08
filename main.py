from web import crear_app
from flask_sqlalchemy import SQLAlchemy

app = crear_app()
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:kQCBSPUMdAGOiWjpYRTXKoZjBWiuHqmF@interchange.proxy.rlwy.net:51042/railway"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)