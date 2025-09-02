# 🧠 Desafio: Reconhecimento Facial com Transfer Learning

Este projeto faz parte do **Bootcamp Machine Learning da BairesDev** promovido pela **DIO.me**, e tem como objetivo aplicar técnicas de **Transfer Learning** para realizar o **reconhecimento facial de múltiplos rostos em uma única imagem**, utilizando modelos de deep learning pré-treinados.

---

## 🎯 Objetivo

Reconhecer os rostos de **Elon Musk**, **Sam Altman** e **Lidiane Jones** em uma imagem de teste, utilizando um banco de dados personalizado com imagens de referência para cada pessoa.

---

## 🗂️ Estrutura do Projeto

- `faces_db/`: pasta contendo imagens de referência para cada pessoa (ex: `sam1.png`, `elon2.png`, `lidiane3.png`)
- `test_1/test_1.png`: imagem de teste contendo múltiplos rostos
- `desafio_reconhecimento_facial.ipynb`: notebook principal desenvolvido no Google Colab

---

## 🧪 Tecnologias Utilizadas

- **DeepFace**: biblioteca de reconhecimento facial que encapsula modelos pré-treinados como VGG-Face, Facenet, ArcFace, entre outros
- **VGG-Face**: modelo de deep learning utilizado para extração de embeddings faciais
- **OpenCV**: para leitura de imagens, desenho de bounding boxes e exibição dos resultados
- **Matplotlib**: para visualização das imagens processadas
- **Google Drive**: utilizado como repositório de dados no ambiente Colab

---

## ⚙️ Funcionalidades Implementadas

- Detecção de múltiplos rostos em uma imagem
- Extração de embeddings faciais com o modelo VGG-Face
- Comparação com banco de dados personalizado usando métrica de distância cosseno
- Identificação dos rostos com nomes completos em caixa alta
- Exibição da imagem final com bounding boxes e nomes reconhecidos

---

## 📌 Transfer Learning na Prática

Este projeto utiliza **Transfer Learning** ao reaproveitar o modelo pré-treinado `VGG-Face`, que já foi treinado com milhões de imagens de rostos. Em vez de treinar um modelo do zero, aplicamos esse conhecimento para reconhecer rostos específicos com um banco de dados pequeno e personalizado.

---

## 📷 Exemplo de Resultado

A imagem de teste é processada e os rostos são identificados com caixas verdes e os seguintes nomes:

- **SAM ALTMAN**  
- **ELON MUSK**  
- **LIDIANE JONES**

---

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Cantalixto/desafios-bairesdev.git
2. Acesse a pasta do projeto:
   ```bash
   cd desafios-bairesdev/desafio-reconhecimento-facial
3. Abra o notebook desafio_reconhecimento_facial.ipynb no Google Colab
4. Certifique-se de montar o Google Drive e ajustar os caminhos para os dados
5. Execute todas as células para visualizar os resultados

---

## 🧠 Aprendizados

- Aplicação prática de Transfer Learning com modelos de reconhecimento facial
- Manipulação de imagens e embeddings faciais
- Integração de múltiplas bibliotecas para visão computacional
- Organização de dados e visualização de resultados em notebooks interativos
