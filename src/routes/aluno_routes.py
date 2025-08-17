from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.services.aluno_service import AlunoService
from src.services.curso_service import CursoService

aluno_bp = Blueprint('aluno', __name__, url_prefix='/alunos')

@aluno_bp.route('/')
def listar():
    alunos = AlunoService.listar_alunos()
    return render_template('aluno/list.html', alunos=alunos)

@aluno_bp.route('/novo', methods=['GET', 'POST'])
def novo():
    cursos = CursoService.listar_cursos()
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        idade = request.form['idade']
        curso_id = request.form['curso_id']
        AlunoService.criar_aluno(nome, email, idade, curso_id)
        flash('Aluno criado com sucesso!')
        return redirect(url_for('aluno.listar'))
    return render_template('aluno/create.html', cursos=cursos)

@aluno_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    aluno = AlunoService.buscar_aluno(id)
    cursos = CursoService.listar_cursos()
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        idade = request.form['idade']
        curso_id = request.form['curso_id']
        AlunoService.atualizar_aluno(aluno, nome, email, idade, curso_id)
        flash('Aluno atualizado com sucesso!')
        return redirect(url_for('aluno.listar'))
    return render_template('aluno/edit.html', aluno=aluno, cursos=cursos)

@aluno_bp.route('/deletar/<int:id>', methods=['GET', 'POST'])
def deletar(id):
    aluno = AlunoService.buscar_aluno(id)
    if request.method == 'POST':
        AlunoService.deletar_aluno(aluno)
        flash('Aluno excluído com sucesso!')
        return redirect(url_for('aluno.listar'))
    return render_template('aluno/delete.html', aluno=aluno)