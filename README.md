# atividadeavaliativades.web2bim
# Atividade Avaliativa - Web 2º BIM

## Entidades do Sistema

- **Aluno**
  - `id`: Identificador único do aluno
  - `nome`: Nome do aluno
  - `email`: E-mail do aluno
  - `idade`: Idade do aluno
  - `curso_id`: Referência ao curso em que o aluno está matriculado

- **Curso**
  - `id`: Identificador único do curso
  - `nome`: Nome do curso
  - `descricao`: Descrição do curso
  - `carga_horaria`: Carga horária do curso

## Relacionamento

- **Aluno pertence a um Curso**  
  Cada aluno pode estar matriculado em um curso.  
  Um curso pode ter vários alunos (relacionamento 1:N entre Curso e Aluno).

## Como executar o projeto

1. **Clone ou baixe o repositório.**

2. **Crie a pasta `instance` na raiz do projeto (no mesmo nível do `app.py`).**
   - Ela deve ficar vazia. O arquivo do banco será criado automaticamente.

3. **Instale as dependências:**