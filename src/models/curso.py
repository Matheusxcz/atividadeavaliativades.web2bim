from src.database import db

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    carga_horaria = db.Column(db.Integer, nullable=False)

    alunos = db.relationship('Aluno', back_populates='curso', cascade='all, delete-orphan')