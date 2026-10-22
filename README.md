# Minha Primeira API com Python

Este projeto marca o início dos meus estudos sobre desenvolvimento de APIs utilizando Python. O objetivo é aprender os fundamentos da criação de aplicações backend, organização de código e comunicação por meio de requisições HTTP.

## Tecnologias utilizadas

- **Python** — linguagem de programação.
- **FastAPI** — framework para desenvolvimento de APIs.
- **Uvicorn** — servidor ASGI para executar a aplicação.
- **Git e GitHub** — versionamento e compartilhamento do código.

## Estrutura do projeto

```text
aula01/
├── main.py
├── .gitignore
└── README.md
```

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd aula01
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

No Linux (Fedora):

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install fastapi uvicorn
```

### 5. Execute a API

```bash
uvicorn main:app --reload
```

A API estará disponível em:

http://127.0.0.1:8000

## Documentação interativa

O FastAPI gera automaticamente uma documentação interativa para testar os endpoints.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Objetivos de aprendizagem

- Compreender o funcionamento de uma API.
- Aprender sobre requisições e respostas HTTP.
- Conhecer os métodos GET, POST, PUT e DELETE.
- Entender como funcionam os endpoints.
- Desenvolver aplicações backend com Python.
- Aprender a testar APIs e documentar projetos.

## Próximos passos

- Criar novos endpoints.
- Implementar validação de dados.
- Aprender a receber dados por meio de requisições POST.
- Integrar a API a um banco de dados.
- Implementar operações CRUD.
- Desenvolver testes automatizados.

## Autor

**William Gabriel Roque de Assis**

Estudante de programação com foco em desenvolvimento backend, APIs e construção de sistemas.

- GitHub: [william-grassis67](https://github.com/william-grassis67)

---

*Projeto desenvolvido para fins de estudo e evolução prática em desenvolvimento backend com Python.*
