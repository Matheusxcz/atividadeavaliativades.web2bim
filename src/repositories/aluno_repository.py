from src.models.aluno import Aluno
from src.database import db

class AlunoRepository:
    @staticmethod
    def get_all():
        return Aluno.query.all()

    @staticmethod
    def get_by_id(aluno_id):
        return Aluno.query.get(aluno_id)

    @staticmethod
    def add(aluno):
        db.session.add(aluno)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(aluno):
        db.session.delete(aluno)
        db.session.commit()