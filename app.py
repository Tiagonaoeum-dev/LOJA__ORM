from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # libera acesso do HTML

# ALTERAÇÃO:
# Antes usávamos sqlite3 manualmente.
# Agora o SQLAlchemy com a URI do banco.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ALTERAÇÃO:
# Inicialização do ORM (Object Relational Mapper)
db = SQLAlchemy(app)


# ALTERAÇÃO:
# Uma CLASSE que representa a tabela (Modelo)
# Não precisa mais escrever SQL manual para tudo
class Jogo(db.Model):
    __tablename__ = 'jogos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)

    # ALTERAÇÃO:
    # Método auxiliar para converter objeto → JSON
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "preco": self.preco,
            "estoque": self.estoque
        }


# ALTERAÇÃO:
# Criar banco automaticamente ao iniciar
with app.app_context():
    db.create_all()


# GET - Listar todos
@app.route('/jogos', methods=['GET'])
def listar_jogos():
    # ALTERAÇÃO:
    # Substitui SELECT * FROM jogos
    jogos = Jogo.query.all()
    return jsonify([j.to_dict() for j in jogos]), 200


# GET - Buscar por ID
@app.route('/jogos/<int:id>', methods=['GET'])
def buscar_jogo(id):
    # ALTERAÇÃO:
    # Substitui SELECT WHERE id = ?
    jogo = Jogo.query.get(id)

    if jogo:
        return jsonify(jogo.to_dict()), 200
    return jsonify({"erro": "Jogo não encontrado"}), 404


# POST - Inserir
@app.route('/jogos', methods=['POST'])
def inserir_jogo():
    dados = request.get_json()

    # ALTERAÇÃO:
    # Criamos objeto em vez de INSERT SQL
    novo_jogo = Jogo(
        titulo=dados.get('titulo'),
        genero=dados.get('genero'),
        preco=dados.get('preco'),
        estoque=dados.get('estoque')
    )

    db.session.add(novo_jogo)   # adiciona na sessão
    db.session.commit()         # salva no banco

    return jsonify({"mensagem": "Jogo criado com sucesso!"}), 201


# PUT - Atualizar
@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    dados = request.get_json()

    jogo = Jogo.query.get(id)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    # ALTERAÇÃO:
    # Atualização direta no objeto (sem SQL)
    jogo.titulo = dados.get('titulo')
    jogo.genero = dados.get('genero')
    jogo.preco = dados.get('preco')
    jogo.estoque = dados.get('estoque')

    db.session.commit()

    return '', 204


# DELETE - Remover
@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    jogo = Jogo.query.get(id)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    # ALTERAÇÃO:
    # Remoção via ORM
    db.session.delete(jogo)
    db.session.commit()

    return jsonify({"mensagem": f"Jogo '{jogo.titulo}' removido!"}), 200


if __name__ == '__main__':
    app.run(debug=True)