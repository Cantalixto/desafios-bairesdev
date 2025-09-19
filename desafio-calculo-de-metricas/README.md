# 📊  Desafio de Projeto: Cálculo de Métricas de Avaliação de Desempenho

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

## 📂 Estrutura do Projeto

```
desafio-calculo-de-metricas/
├── dados/
│   └── dataset.csv
├── src/
│   └── analise_metricas.py
├── README.md
```

---

## ▶️ Como Executar o Projeto
### Passo 1: Clone o Repositório

Para obter o código, use o comando `git clone` no seu terminal:

```bash
git clone [https://github.com/Cantalixto/desafios-bairesdev.git](https://github.com/Cantalixto/desafios-bairesdev.git)
```
Em seguida, navegue até a pasta específica do projeto:
```bash
cd desafios-bairesdev/desafio-calculo-de-metricas
```
### Passo 2: Execute o Código

O projeto não requer bibliotecas externas, mas você pode precisar de um ambiente com Python. Para rodar o script e ver os resultados das métricas, execute o seguinte comando:
```bash
python src/analise_metricas.py
```

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

## 💡 Aprendizados

Este desafio reforça a importância de avaliar modelos além da acurácia, especialmente em contextos sensíveis como saúde, onde falsos negativos podem ter consequências críticas.

---

## ❤️ Como Contribuir ou Apoiar

Se este repositório foi útil para você, considere dar uma estrela ⭐️ no canto superior direito para me apoiar. Isso me motiva a continuar criando conteúdo e projetos de qualidade.

Se você deseja usar este projeto como base para o seu próprio trabalho ou propor melhorias, sinta-se à vontade para dar um fork no repositório.
1. Faça o Fork: Clique no botão "Fork" no canto superior direito desta página.
2. Clone o Repositório: Clone o seu fork para sua máquina local.
3. Faça suas Alterações: Crie uma nova branch, faça suas alterações e suba o código.
4. Abra um Pull Request: Envie um Pull Request para que suas alterações possam ser revisadas e, se aprovadas, mescladas ao projeto original.

---

