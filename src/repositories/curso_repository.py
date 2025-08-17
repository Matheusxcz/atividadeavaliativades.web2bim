from src.models.curso import Curso
from src.database import db

class CursoRepository:
    @staticmethod
    def get_all():
        return Curso.query.all()

    @staticmethod
    def get_by_id(curso_id):
        return Curso.query.get(curso_id)

    @staticmethod
    def add(curso):
        db.session.add(curso)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(curso):
        db.session.delete(curso)
        db.session.commit()