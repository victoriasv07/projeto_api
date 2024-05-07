from flask import Blueprint, jsonify, request
from random_data import pessoas
import  funcoes


bp = Blueprint("api", __name__)


@bp.route('/')
def index():
    return jsonify({"status": 200, "message": "API do VICTORIA_SILVA_VIEIRA"})

@bp.route("/api/aleatorios")
def aleatorios():
    import random
    a = random.randint(49,100)
    return jsonify({"status": 200, "data": a})


@bp.route('/api/argumentos/<string:nome>')
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})


@bp.route("/api/maior_de_50", methods=["GET"])
def maior_de_50():
    count = funcoes.maior_de_50(pessoas)
    return jsonify({"status": 200, "Pessoas com mais de 50 anos:": count})

@bp.route("/api/mais_2000", methods=["GET"])
def mais_2000():
    count, x, total_registros = funcoes.mais_2000(pessoas)
    return jsonify({"status": 200, "Pessoas com registros": total_registros, "Pessoas que ganham mais de 2000:": count, "Porcentagem de pessoas que ganham 2000:": x})

@bp.route("/api/media_profissoes", methods=["GET"])
def media_profissoes():
    profissoes = funcoes.media_profissoes(pessoas)
    return jsonify({"status": 200, "Descrição das profissões:": profissoes})

@bp.route("/api/tres_maiores", methods=["GET"])
def tres_maiores():
    tres_maiores = funcoes.tres_salarios(pessoas)
    return jsonify({"status": 200, "Os três maiores salários": tres_maiores})

@bp.route("/api/sexo_idades", methods=["GET"])
def sexo_idades():
    count_feminino, count_masculino, intervalo_idades, sexo_maior_2000 = funcoes.sexo_idade(pessoas)
    return jsonify({"status": 200, "Mulheres que ganham mais de 2000": count_feminino, "Homens que ganham mais de 2000": count_masculino, "intervalo da idade de quem ganha mais de 2000": intervalo_idades, "Sexo que há mais pessoas que ganham mais de 2000": sexo_maior_2000})

