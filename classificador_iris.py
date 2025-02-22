import gradio as gr
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Carregar o conjunto de dados
iris = load_iris()
X = iris.data
y = iris.target

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
modelo = RandomForestClassifier(n_estimators=100)
modelo.fit(X_train, y_train)

# Criar a interface de usuário com Gradio
def classify(sepal_length, sepal_width, petal_length, petal_width):
    entrada = [[sepal_length, sepal_width, petal_length, petal_width]]
    predicao = modelo.predict(entrada)
    return iris.target_names[predicao[0]]

interface = gr.Interface(
    fn=classify,
    inputs=[
        gr.Number(label="Comprimento da sépala"),
        gr.Number(label="Largura da sépala"),
        gr.Number(label="Comprimento da pétala"),
        gr.Number(label="Largura da pétala"),
    ],
    outputs=gr.Label(label="Espécie de Iris"),
    title="Classificador de Iris",
    description="Insira as características da flor de iris para obter a classificação",
)

# Iniciar a interface
interface.launch()