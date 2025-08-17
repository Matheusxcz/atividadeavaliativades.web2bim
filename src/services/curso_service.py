from src.repositories.curso_repository import CursoRepository
from src.models.curso import Curso

class CursoService:
    @staticmethod
    def listar_cursos():
        return CursoRepository.get_all()

    @staticmethod
    def buscar_curso(curso_id):
        return CursoRepository.get_by_id(curso_id)

    @staticmethod
    def criar_curso(nome, descricao, carga_horaria):
        curso = Curso(nome=nome, descricao=descricao, carga_horaria=carga_horaria)
        CursoRepository.add(curso)

    @staticmethod
    def atualizar_curso(curso, nome, descricao, carga_horaria):
        curso.nome = nome
        curso.descricao = descricao
        curso.carga_horaria = carga_horaria
        CursoRepository.update()

    @staticmethod
    def deletar_curso(curso):
        CursoRepository.delete(curso)