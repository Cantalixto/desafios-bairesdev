# 📊 Desafio: Análise de Métricas de Classificação

Este projeto é parte do meu repositório **desafios-bairesdev** e foca na prática de avaliação de modelos de Machine Learning.  
O objetivo foi aplicar conceitos de métricas de classificação para analisar o desempenho de um modelo em um problema real na área da saúde.

---

## 🧬 O Problema

O desafio consiste em criar um modelo de classificação binária para prever a presença de câncer de mama com base em características de células mamárias.  
O dataset utilizado é o **Breast Cancer Wisconsin**, que contém dados sobre tumores classificados como benignos ou malignos.

---

## 💻 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal  
- **Scikit-learn**: Para carregamento do dataset (`load_breast_cancer`), divisão dos dados (`train_test_split`) e treinamento do modelo (`LogisticRegression`)  
- **NumPy**: Para manipulação de arrays e dados numéricos  
- **Matplotlib** e **Seaborn**: Para a visualização da matriz de confusão

---

## 🔬 Métricas de Avaliação

O ponto central deste desafio foi a implementação e análise manual de métricas de avaliação, focando em entender o significado de cada uma no contexto do problema:

- **Matriz de Confusão**: Tabela que resume o desempenho do modelo, mostrando a contagem de Verdadeiros Positivos, Verdadeiros Negativos, Falsos Positivos e Falsos Negativos  
- **Acurácia**: Proporção de previsões corretas em relação ao total  
- **Precisão**: Capacidade do modelo de evitar falsos alarmes. No contexto deste problema, indica a confiabilidade do modelo ao prever que um tumor é maligno  
- **Revocação (Recall)**: Capacidade do modelo de encontrar todos os casos positivos. Métrica crítica, pois um Falso Negativo (classificar um tumor maligno como benigno) pode ter consequências graves  
- **F1-Score**: Média harmônica que equilibra Precisão e Revocação

---

## ⚙️ Como Rodar o Código

1. Clone este repositório para sua máquina  
2. Abra o arquivo `.py` em um ambiente de desenvolvimento Python  
3. Instale as bibliotecas necessárias com `pip install -r requirements.txt` (ou instale-as individualmente)  
4. Execute o script para ver os resultados da avaliação do modelo

---

## ✅ Resultados

Os resultados do modelo de **Regressão Logística** demonstraram alta eficácia, especialmente na **Revocação**, o que indica uma baixa taxa de Falsos Negativos.  
Isso torna o modelo promissor para uso em um contexto de triagem, onde a capacidade de identificar todos os casos positivos é de extrema importância.
