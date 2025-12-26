# Importa o modelo Carro pasta models
from models.carro_models import Carro
# Importa a instancia do banco de dados
from db import db
# Importa a biblioteca json para manipulção de dados em formato JSON
import json
# Importa a função make_response do flask para criar respostas personalizadas
from flask import make_response

def create_carro(carrro_data):

    # Cria uma nova instancia da classe Carro com os dados fornecidos
    novo_carro = Carro(
        modelo=carro_data['modelo'],
        marca=carro_data['marca'],
        ano=carro_data['ano']
    )

    # Adiciona o novo carro á sessão do banco de dados
    db.session.add(novo_carro)
    # Confirma a transação para salvar o novo carro no banco
    db.session.commit()

    # Cria uma resposta HTTP personalizada no formato JSON
    response = make_response(
        json.dumps({
            'mensagem': 'Carro cadastrado com sucesso!', # Mensagem de sucesso
            'carro': novo_carro.json() # Dados do carro cadastrado    
        }, sort_keys=False) # Mantem a ordem dos campos no JSON
    )

    # Define o cabecalho da resposta como JSON
    response.headers['Content-Type'] = 'application/json'

    # Retorna a resposta para o cliente
    return response
