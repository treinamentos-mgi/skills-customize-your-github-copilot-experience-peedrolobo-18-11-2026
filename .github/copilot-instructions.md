# Instrucoes do GitHub Copilot

## Descricao do projeto

Este projeto e um site educacional para compartilhar tarefas e exercicios de programacao com os alunos. O portal permite navegar, visualizar e baixar tarefas.

- `assignments/` armazena cada tarefa em sua propria subpasta, seguindo uma estrutura consistente.
- `templates/` contem modelos reutilizaveis para novo conteudo.
- `assets/` contem os recursos do site, incluindo CSS, JavaScript e imagens.
- `index.html` e a pagina principal do portal estatico.
- `config.json`, na raiz do repositorio, configura os dados do curso e as tarefas exibidas no portal.

## Diretrizes do projeto

- Mantenha um estilo consistente em todas as paginas.
- Use nomes de arquivos e pastas descritivos e organizados.
- Preserve a arquitetura existente: HTML, CSS e JavaScript sem framework no portal; Python nos exercicios.
- Evite adicionar dependencias, ferramentas de build ou novos arquivos de configuracao sem necessidade.
- Ao alterar uma tarefa, mantenha seus arquivos e caminhos consistentes com as demais tarefas.
- Preserve os seletores HTML usados por `assets/js/`, os caminhos relativos entre paginas e a apresentacao responsiva existente.
- Use `textContent` para inserir texto dinamico quando HTML nao for necessario. Se gerar HTML dinamico, nao insira conteudo externo ou nao confiavel sem sanitizacao.
- Mantenha as alteracoes focadas e siga o estilo do arquivo que esta sendo editado.

## Padroes educacionais

- Defina objetivos de aprendizado claros e escolha um nivel de dificuldade apropriado para os alunos.
- Use linguagem clara, acolhedora e encorajadora.
- Documente os requisitos em `README.md` e deixe no codigo inicial apenas o necessario para o aluno completar a atividade; nao inclua uma solucao completa sem solicitacao explicita.

## Convencoes

- Use `config.json` como fonte de dados do curso e da lista de exercicios. Ao adicionar ou alterar um exercicio, mantenha os campos e caminhos consistentes com os ja existentes.
- Cada exercicio fica em `assignments/<id>/` e deve seguir os nomes de arquivo existentes, como `README.md`, `starter-code.py` e, quando necessario, `data.csv`.

## Validacao

- Para mudancas no catalogo, confira se `config.json` continua sendo JSON valido e se cada caminho de exercicio aponta para os arquivos existentes.
- Para mudancas nos exercicios, use `assets/extra/hooks/validate-assignment-structure.py` quando apropriado para conferir os nomes de arquivo permitidos.
- Nao presuma que existe uma suite de testes ou processo de build; verifique os recursos disponiveis antes de propor comandos de validacao.