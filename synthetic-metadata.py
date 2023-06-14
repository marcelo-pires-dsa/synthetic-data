# SingleTable Synthetic metadata
# Author: Marcelo Pires <marcelopires@usp.br>

# Importar a biblioteca do sdv para carregar o dataset real que servirá de base
# Esse dataset é usado para o sdv capturar o comportamento do dataset
from sdv.datasets.local import load_csvs
# Importar a biblioteca para gerar os metadados referentes as variáveis do dataset de base
# de modo que o sdv possa syntetizar corretamente nossos dados
from sdv.metadata import SingleTableMetadata

dataset  = load_csvs(folder_name="dataset/raw/")
support_ticket = dataset["customer_support_tickets_processed"]

# Gerar os metadados para dataset base. Usando o auto detect
# O objet metadata terá uma propriedade `columns` onde podemos conferir, se as variáveis
# foram corretamente identificados

metadata.detect_from_csv(filepath="dataset/raw/customer_support_tickets_processed.csv")

# Atualizando o tipo da coluna, caso contrário teremos o erro
# The primary_keys ['ticket_id'] must be type 'id' or another PII type.
metadata.update_column(
    column_name='ticket_id',
    sdtype='id'
)

# Definindo a chave primária `Ticket.ID
metadata.set_primary_key(column_name='ticket_id')
# Criando um dicionário com os atributos dos metadados
metadata_dict = metadata.to_dict()

# Caso tenhamos algum problema o método validate exibirá todos os erros
metadata.validate()

# Salvando o arquivo de metadados
metadata.save_to_json(filepath='./synthetic-dataset-metadata.json')