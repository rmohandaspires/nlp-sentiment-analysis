# 📝 NLP Sentiment Analysis

Este projeto implementa um sistema de **análise de sentimentos** em textos utilizando técnicas de **Processamento de Linguagem Natural (NLP)** e **Machine Learning**.  
O modelo classifica textos (como avaliações de produtos ou comentários) em **positivos** ou **negativos**.

---

## 🚀 Tecnologias Utilizadas
- Python 3.10+
- Scikit-learn
- Pandas & NumPy
- Joblib (para salvar/carregar o modelo)
- Flask / FastAPI (para disponibilizar a API)
- Jupyter Notebook (para testes e experimentos)

---

```bash
nlp-sentiment-analysis/
│-- analise_de_sentimentos/
│   ├── app.py              # API para consumo do modelo
│   ├── treino.py           # Treinamento do classificador
│   ├── modelo.joblib       # Modelo treinado salvo
│   ├── requirements.txt    # Dependências do projeto
│-- venv/                   # Ambiente virtual (ignorado pelo Git)
│-- README.md               # Documentação
│-- .gitignore

## ⚙️ Instalação

Clone este repositório:
```bash
git clone https://github.com/rmohandaspires/nlp-sentiment-analysis.git
cd nlp-sentiment-analysis

Crie um ambiente virtual e instale as dependências:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r analise_de_sentimentos/requirements.txt

🏋️ Treinamento do Modelo

Execute o script de treinamento:
python analise_de_sentimentos/treino.py

O modelo será salvo em analise_de_sentimentos/modelo.joblib.

▶️ Executando a Aplicação
Rode a aplicação (Flask ou FastAPI):
python analise_de_sentimentos/app.py

A API ficará disponível em:
http://127.0.0.1:5000

📊 Exemplo de Uso
Requisição (POST)
{
  "texto": "O produto é excelente, gostei muito!"
}

Resposta
{
  "sentimento": "positivo"
}

📌 Próximos Passos

Melhorar pré-processamento dos textos (remoção de stopwords, stemming/lemmatização).

Testar diferentes algoritmos de classificação (SVM, RandomForest, redes neurais).

Criar dashboard simples para visualizar estatísticas de sentimentos.

👨‍💻 Autor

Projeto desenvolvido por Raphael Mohandas.
