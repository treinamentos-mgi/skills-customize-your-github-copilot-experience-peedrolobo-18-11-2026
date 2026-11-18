# 📘 Atividade: Testando APIs com pytest

## 🎯 Objetivo

Pratique testes automatizados para APIs FastAPI usando pytest e TestClient. Você verificará respostas corretas, casos de erro e validação de dados sem precisar alterar a implementação da API.

## 📝 Tarefas

### 🛠️ Testar os endpoints de leitura

#### Descrição

Copie `starter-code.py` para `main.py` no seu ambiente de trabalho e crie `test_api.py`. Instale as dependências com `python -m pip install fastapi pytest httpx` e use o `TestClient` para testar os endpoints existentes.

#### Requisitos

O programa de testes deve:

- Confirmar que `GET /` responde com status HTTP `200` e uma mensagem JSON.
- Confirmar que `GET /books` responde com status HTTP `200` e retorna os livros como uma lista.
- Executar com `pytest -q`.

### 🛠️ Testar busca e respostas de erro

#### Descrição

Adicione testes para consultar um livro existente por ID e para solicitar um ID que não existe. Verifique tanto o status HTTP quanto os dados relevantes da resposta.

#### Requisitos

O programa de testes deve:

- Confirmar que `GET /books/{book_id}` retorna status `200` e o livro correspondente para um ID existente.
- Confirmar que a busca por um ID inexistente retorna status `404`.
- Confirmar que a resposta de erro inclui o detalhe `Book not found`.

### 🛠️ Testar criação e validação de dados

#### Descrição

Teste a criação de um livro com dados válidos e uma requisição incompleta. Mantenha os testes independentes: restaure a lista de livros entre testes ou use dados únicos e não dependa da ordem de execução.

#### Requisitos

O programa de testes deve:

- Confirmar que `POST /books` com `title` e `author` retorna status `201` e o livro criado com um ID.
- Confirmar que o livro criado aparece em uma chamada posterior a `GET /books`.
- Confirmar que dados sem um campo obrigatório retornam status `422`.
- Continuar passando ao executar toda a suíte com `pytest -q`.