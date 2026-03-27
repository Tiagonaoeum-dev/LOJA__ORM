# API Loja de Jogos

## Descrição

API REST desenvolvida com Python, Flask e Flask-SQLAlchemy para gerenciamento de uma loja de jogos online.

O sistema permite realizar operações completas de CRUD (Create, Read, Update, Delete) em um banco de dados SQLite.

---

## Tecnologias Utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- JSON

---

## Funcionalidades

- Listar todos os jogos
- Buscar jogo por ID
- Inserir novo jogo
- Atualizar jogo existente
- Deletar jogo

---

## Estrutura do Projeto

```
projeto/
│
├── app.py
├── loja.db
├── README.md
├── static/
│   └── style.css
└── templates/
    └── index.html
```

---

## Como Executar o Projeto

### 1. Clonar o repositório
```
git clone https://github.com/Tiagonaoeum-dev/LOJA__ORM
```

### 2. Instalar dependências
```
pip install flask flask_sqlalchemy flask-cors
```

### 3. Executar a aplicação
```
python app.py
```

A API estará disponível em:
```
http://127.0.0.1:5000/jogos
```

---

## Endpoints da API

### Listar todos os jogos
```
GET /jogos
```

### Buscar jogo por ID
```
GET /jogos/{id}
```

### Inserir novo jogo
```
POST /jogos
```

### Atualizar jogo
```
PUT /jogos/{id}
```

### Deletar jogo
```
DELETE /jogos/{id}
```

---

## Exemplos de Requisições (cURL)

### Inserir jogo
```
curl -X POST http://127.0.0.1:5000/jogos \
-H "Content-Type: application/json" \
-d "{\"titulo\":\"GTA V\",\"genero\":\"Ação\",\"preco\":99.90,\"estoque\":15}"
```

### Atualizar jogo
```
curl -X PUT http://127.0.0.1:5000/jogos/1 \
-H "Content-Type: application/json" \
-d "{\"titulo\":\"GTA V\",\"genero\":\"Ação\",\"preco\":89.90,\"estoque\":10}"
```

### Deletar jogo
```
curl -X DELETE http://127.0.0.1:5000/jogos/1
```

---

## Testes com Thunder Client

A API pode ser testada utilizando a extensão Thunder Client no VS Code:

- Criar requisições GET, POST, PUT e DELETE
- Utilizar JSON no body das requisições
- Configurar header:
```
Content-Type: application/json
```

---

## Alterações com ORM (Flask-SQLAlchemy)

- Substituição do uso direto do sqlite3 pelo ORM Flask-SQLAlchemy
- Criação da classe `Jogo` representando a tabela
- Uso de métodos como:
  - `query.all()`
  - `query.get()`
  - `session.add()`
  - `session.commit()`
  - `session.delete()`
- Redução de código SQL manual
- Melhor organização e manutenção do código

---

## Padrões Utilizados

- Arquitetura REST
- Comunicação via JSON
- Separação de responsabilidades (modelo e rotas)
- Uso de ORM para abstração do banco de dados

---

## Interface Web

O projeto também possui uma interface HTML + CSS que consome a API e exibe os jogos em formato de cards, simulando uma loja online.

---

## Status HTTP Utilizados

- 200 OK
- 201 Created
- 204 No Content
- 404 Not Found

---

## HTML e CSS
Como sou da area do design fiz uma pequena demonstração dos dados sendo apresentados em tela. Assim que um jogo e adcionado ele aparece visualmente no navegador. Ainda estou preparando o codigo para futuras atualizações para que seja incluso pelo proprio navegador com acesso administrativo.

## Autor
Tiagonaoeum-dev

Projeto desenvolvido para fins acadêmicos.
