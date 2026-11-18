# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI usando rotas, parâmetros de caminho, validação de dados e códigos de status HTTP. Ao final, você terá uma API simples para consultar e cadastrar livros.

## 📝 Tarefas

### 🛠️ Criar endpoints de leitura

#### Descrição

Complete os endpoints iniciais para apresentar a API e listar os livros guardados na lista em memória. Para executar o projeto, instale FastAPI e Uvicorn e inicie a aplicação com `python -m uvicorn starter-code:app --reload`.

#### Requisitos

O programa concluído deve:

- Responder a `GET /` com uma mensagem em JSON que identifique a API.
- Responder a `GET /books` com a lista de livros existente.
- Exibir a documentação interativa do FastAPI em `/docs`.

### 🛠️ Buscar um livro pelo ID

#### Descrição

Implemente a rota de leitura de um livro específico. Use o parâmetro de caminho `book_id` para localizar o livro na lista em memória.

#### Requisitos

O programa concluído deve:

- Responder a `GET /books/{book_id}` com o livro correspondente ao ID informado.
- Retornar o status HTTP `404` com uma mensagem clara quando o ID não existir.

### 🛠️ Cadastrar um livro

#### Descrição

Complete o modelo de entrada e o endpoint para cadastrar livros. A rota deve receber os dados do livro em JSON, validar os campos e guardar o novo livro na lista em memória.

#### Requisitos

O programa concluído deve:

- Validar os campos obrigatórios `title` e `author` com um modelo Pydantic.
- Responder a `POST /books` com o novo livro, incluindo um ID único.
- Usar o status HTTP `201` para indicar que o livro foi criado.
- Retornar o novo livro nas chamadas seguintes a `GET /books`.

Exemplo de corpo da requisição:

```json
{
  "title": "The Little Prince",
  "author": "Antoine de Saint-Exupery"
}
```