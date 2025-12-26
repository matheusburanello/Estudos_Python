# Importa a instancia do banco de dados do arquivo db.py
from db import db

# Define a classe Carro, que representa a tabela 'carro' no banco de dados
class Carro(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'carro'

    # Define a coluna 'id' como chave primaria, do tipo inteiro e atuo-incrementavwl
    id = db.Column(db.Integer, primary_key=True)

    # Define a coluna 'modelo', do tipo string com até 80 caracteres, não pode ser nula
    model = db.Column(db.String(80), nullable=False)

    # Define a coluna 'marca', do tipo string com até 80 caracteres, não pode ser nula
    marca = db.Column(db.String(80), nullable=False)

    # Define a coluna 'ano', do tipo inteiro, não pode ser nula
    ano = db.Column(db.Integer, nullable=False)

    def json(self):
        """
        Metodo que retorna os dados do carro em formato JSON

        Retorno:
        dict: Dicionario com os dados do carro
        """
        return {
            'id': self.id,
            'modelo': self.model,
            'marca': self.marca,
            'ano': self.ano
        }
        