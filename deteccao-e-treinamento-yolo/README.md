# Detecção de Objetos: Leitos Hospitalares e Monitores

Este projeto foi desenvolvido como parte do *Desafio de Projeto: Criação de uma Base de Dados e Treinamento da Rede YOLO*, do curso de Machine Learning da BairesDev na DIO.me. O objetivo principal era rotular uma base de dadose aplicar o treinamento com a rede YOLO.

---

Este projeto utiliza o modelo *YOLOv8* para detectar e identificar o status de leitos hospitalares (ocupado/desocupado) e monitores multiparâmetros (ligado/desligado) em imagens. O objetivo é criar uma solução automatizada para monitoramento de ambientes hospitalares, melhorando a gestão de recursos e a eficiência operacional.

---

## 🚀 Como o Projeto Foi Desenvolvido

### 1. Coleta de Dados e Anotação
O projeto começou com um conjunto inicial de imagens de leitos e monitores hospitalares. Os objetos foram manualmente *anotados* com caixas de delimitação (bounding boxes) e classificados em quatro categorias:

* leito-hospitalar-desocupado
* leito-hospitalar-ocupado
* monitor-multiparametros-desligado
* monitor-multiparametros-ligado

Para melhorar o desempenho e evitar o overfitting, o dataset foi expandido para *75 imagens* através de técnicas de *aumento de dados (data augmentation)*, como rotações, mudanças de brilho e zoom.

### 2. Treinamento do Modelo
O modelo de detecção de objetos *YOLOv8n* (a versão "nano" do YOLOv8) foi treinado por *50 épocas* em uma GPU, utilizando o dataset anotado. Durante o treinamento, o modelo foi capaz de aprender os padrões visuais de cada classe, alcançando um alto nível de precisão.

### 3. Resultados e Avaliação
O modelo foi avaliado em um conjunto de imagens que ele nunca tinha visto antes, demonstrando um desempenho notável na identificação dos objetos. As principais métricas de avaliação foram:

* *mAP50: [0.995*]
* *mAP50-95: [0.96598*]

As previsões do modelo em novas imagens podem ser vistas na pasta /runs/detect/.

---

## 💾 Dataset
O dataset completo utilizado neste projeto é público e está disponível no Roboflow. Ele inclui as imagens originais, já devidamente rotuladas com as caixas de anotação (bounding boxes) e as classes correspondentes.

*Link para o Dataset:*

https://app.roboflow.com/leito-hospitalar/leito-hospitalar-d7f3j/5

---

## 🛠️ Tecnologias Utilizadas

* *YOLOv8*: O modelo de detecção de objetos de última geração.
* *Ultralytics*: A biblioteca Python que implementa o YOLOv8.
* *Roboflow*: Plataforma usada para gerenciar o dataset e realizar anotações e aumento de dados.
* *Google Colab*: Ambiente de desenvolvimento para o treinamento do modelo em GPU.

## 📁 Estrutura do Projeto

* notebook.ipynb: O notebook do Google Colab com todo o código-fonte para o treinamento e a predição.
* best.pt: O modelo treinado, pronto para ser utilizado em novas imagens ou em outras aplicações.
* /runs/detect/predict: Pasta contendo as imagens com as predições do modelo.

---

## 💻 Como Usar o Projeto

Siga os passos abaixo para rodar este projeto no seu próprio ambiente do Google Colab.

1.  **Faça o Upload do Dataset**: Faça o download do dataset no Roboflow e envie o arquivo `.zip` para o seu ambiente no Google Colab.
2.  **Crie um Novo Notebook**: Crie um novo notebook e ative a **GPU** em `Ambiente de execução > Alterar tipo de ambiente de execução`.
3.  **Instale as Dependências**:
    ```bash
    !pip install ultralytics roboflow
    ```
4.  **Descompacte o Dataset**:
    ```bash
    !unzip [nome_do_seu_dataset].zip
    ```
5.  **Treine o Modelo**:
    ```bash
    !yolo task=detect mode=train model=yolov8n.pt data=[nome_da_pasta_do_dataset]/data.yaml epochs=50 imgsz=640
    ```
6.  **Faça a Predição**:
    ```bash
    !yolo task=detect mode=predict model=runs/detect/[nome_da_pasta_do_treinamento]/weights/best.pt source=[caminho_da_pasta_de_teste]
    ```

---    

## ❤️ Como Contribuir ou Apoiar

Se este projeto foi útil para você, considere dar uma **estrela** ⭐️ no repositório. Isso me ajuda a saber que meu trabalho foi relevante!

Se você deseja usar este projeto como base para o seu próprio trabalho ou propor melhorias, sinta-se à vontade para dar um **fork** no repositório.

1.  **Faça o Fork**: Clique no botão "Fork" no canto superior direito desta página.
2.  **Clone o Repositório**: Clone o seu fork para sua máquina local.
3.  **Faça suas Alterações**: Crie uma nova branch, faça suas alterações e suba o código.
4.  **Abra um Pull Request**: Envie um Pull Request para que suas alterações possam ser revisadas e, se aprovadas, mescladas ao projeto original.
