#Importando a biblioteca
#Detalhes sobre o Gaussian Copula Synthesizer, consulte. https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/gaussiancopulasynthesizer
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
from sdv.datasets.local import load_csvs
from sdv.evaluation.single_table import evaluate_quality
import pandas as pd

#Carregando o dataset dataset preparado (Data Wrangling)
dataset  = pd.read_csv('dataset/raw/customer_support_tickets_processed.csv')

#Carregando os metadados
metadata = SingleTableMetadata.load_from_json(
    filepath='synthetic-dataset-metadata.json'
)

#Criar o sintetizador
synthesizer = GaussianCopulaSynthesizer(metadata)

#Trainando
synthesizer.fit(dataset)

#Gerando os dado ssintéticos
#TODO: Verificar o dataset original para Data Wrangling
# pois customer_satisfation_rating no dataset sintético está com valores constantes NA e 3
# reslution, fist_response_time e time_to_resolution com valor não esperados nan
synth_data = synthesizer.sample(num_rows=20000,
                                output_file_path='dataset/synthetic/customer_support_tickets-v3.csv')

#Salvando o synthesizer treinado para uso posterior
#TODO: Use git commit short sha
synthesizer.save(filepath='output/syntesizer-v1.pkl')

# Avaliando a qualidade dos dado ssintéticos
report = evaluate_quality(
    real_data=dataset,
    synthetic_data=synth_data,
    metadata=metadata
)