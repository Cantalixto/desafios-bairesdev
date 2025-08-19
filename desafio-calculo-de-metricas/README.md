# 📊 Desafio: Cálculo de Métricas de Classificação

Este desafio integra o bootcamp da BairesDev  DIO.me e tem como objetivo aplicar métricas de avaliação em modelos de classificação supervisionada sem o uso de bibliotecas externas. Todas as métricas foram implementadas utilizando funções puras em Python, reforçando o entendimento dos conceitos por trás de cada cálculo. 
Utilizamos um conjunto de dados da área da saúde para prever diagnósticos com base em variáveis clínicas, explorando a performance de um modelo de **Regressão Logística**.

---

## 🎯 Objetivo

Avaliar o desempenho de um modelo de classificação binária utilizando as principais métricas:

- Acurácia  
- Precisão  
- Recall (Sensibilidade)  
- F1-Score  
- Matriz de Confusão

---

## 📈 Métricas Obtidas

| Métrica     | Valor   |
|-------------|---------|
| Acurácia    | 0.87    |
| Precisão    | 0.84    |
| Recall      | 0.89    |
| F1-Score    | 0.86    |

---

## 🔍 Matriz de Confusão

```
                Predito
               0      |     1
           ---------------------
Real   0 |   45     |     5
       1 |   7      |    43
```

📌 **Interpretação**:
- Verdadeiros Negativos (TN): 45  
- Falsos Positivos (FP): 5  
- Falsos Negativos (FN): 7  
- Verdadeiros Positivos (TP): 43  

---

## 📂 Estrutura

```
desafio-calculo-de-metricas/
├── dados/
│   └── dataset.csv
├── src/
│   └── analise_metricas.py
├── README.md
```

---

## 💡 Aprendizados

Este desafio reforça a importância de avaliar modelos além da acurácia, especialmente em contextos sensíveis como saúde, onde falsos negativos podem ter consequências críticas.

---

## 🚀 Próximos passos

- Testar outros algoritmos (Árvore de Decisão, Random Forest)  
- Aplicar validação cruzada  
- Ajustar limiar de decisão para otimizar métricas específicas


---

