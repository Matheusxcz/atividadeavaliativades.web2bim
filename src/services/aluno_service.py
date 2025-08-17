from src.repositories.aluno_repository import AlunoRepository
from src.models.aluno import Aluno

class AlunoService:
    @staticmethod
    def listar_alunos():
        return AlunoRepository.get_all()

    @staticmethod
    def buscar_aluno(aluno_id):
        return AlunoRepository.get_by_id(aluno_id)

    @staticmethod
    def criar_aluno(nome, email, idade, curso_id):
        aluno = Aluno(nome=nome, email=email, idade=idade, curso_id=curso_id if curso_id else None)
        AlunoRepository.add(aluno)

    @staticmethod
    def atualizar_aluno(aluno, nome, email, idade, curso_id):
        aluno.nome = nome
        aluno.email = email
        aluno.idade = idade
        aluno.curso_id = curso_id if curso_id else None
        AlunoRepository.update()

    @staticmethod
    def deletar_aluno(aluno):
        AlunoRepository.delete(aluno)