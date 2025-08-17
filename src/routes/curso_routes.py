from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.services.curso_service import CursoService

curso_bp = Blueprint('curso', __name__, url_prefix='/cursos')

@curso_bp.route('/')
def listar():
    cursos = CursoService.listar_cursos()
    return render_template('curso/list.html', cursos=cursos)

@curso_bp.route('/novo', methods=['GET', 'POST'])
def novo():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        carga_horaria = request.form['carga_horaria']
        CursoService.criar_curso(nome, descricao, carga_horaria)
        flash('Curso criado com sucesso!')
        return redirect(url_for('curso.listar'))
    return render_template('curso/create.html')

@curso_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    curso = CursoService.buscar_curso(id)
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        carga_horaria = request.form['carga_horaria']
        CursoService.atualizar_curso(curso, nome, descricao, carga_horaria)
        flash('Curso atualizado com sucesso!')
        return redirect(url_for('curso.listar'))
    return render_template('curso/edit.html', curso=curso)

@curso_bp.route('/deletar/<int:id>', methods=['GET', 'POST'])
def deletar(id):
    curso = CursoService.buscar_curso(id)
    if request.method == 'POST':
        CursoService.deletar_curso(curso)
        flash('Curso excluído com sucesso!')
        return redirect(url_for('curso.listar'))
    return render_template('curso/delete.html', curso=curso)