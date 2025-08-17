from src.database import db

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))

    curso = db.relationship('Curso', back_populates='alunos')