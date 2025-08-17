import os
from flask import Flask, render_template
from src.database import db, init_db
from src.routes.aluno_routes import aluno_bp
from src.routes.curso_routes import curso_bp

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, 'instance', 'escola.db')

app = Flask(__name__, static_folder='src/static', template_folder='src/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db.init_app(app)
init_db(app)

app.register_blueprint(aluno_bp)
app.register_blueprint(curso_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
