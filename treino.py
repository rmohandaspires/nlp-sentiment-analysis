import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Dataset

dados = {
    'texto' : [
        "o produto é ótimo",
        "gostei muito do atendimento",
        "a entrega foi rápida",
        "péssima qualidade",
        "não gostei do serviço",
        "o aplicativo é horrível",
    ],
    "label" :[1, 1, 1 , 0, 0, 0] # 1 para positivo, 0 para negativo 
    }

df = pd.DataFrame(dados)

# Modelo
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

pipeline.fit(df["texto"], df["label"])

# Salvando o modelo
joblib.dump(pipeline, 'modelo.joblib')