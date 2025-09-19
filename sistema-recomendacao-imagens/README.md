# 💡 Desafio de Projeto: Sistema de Recomendação por Imagens Digitais

Este projeto tem como objetivo desenvolver um sistema de recomendação visual utilizando deep learning. A proposta envolve o treinamento de uma rede neural para classificar imagens e a implementação de um sistema de recomendação por similaridade visual.

---

## 🎯 Objetivo

- Treinar uma rede neural com **4 classes de objetos**: `camiseta`, `sapato`, `relógio`, `bolsa`.
- Utilizar **transfer learning** com o modelo `EfficientNetB0`.
- Implementar recomendação por **similaridade visual** com base na classe prevista.
- Permitir que o usuário envie uma imagem externa e receba sugestões visuais semelhantes.

---

## ⚙️ Tecnologias Utilizadas

- Python 3
- TensorFlow / Keras
- EfficientNetB0 (pré-treinado no ImageNet)
- Scikit-learn
- Matplotlib
- Pillow

---

## 📁 Estrutura do Projeto

```bash
sistema-recomendacao-imagens/
├── camiseta/
├── sapato/
├── relogio/
├── bolsa/
├── sistema_recomendacao.ipynb
└── README.md
```

## 📄 Etapas do Projeto

1. **Organização do dataset**  
   Imagens separadas por categoria em pastas específicas.

2. **Data augmentation**  
   Geração de imagens aumentadas para melhorar a robustez do modelo.

3. **Extração de embeddings**  
   Utilização do EfficientNetB0 para transformar imagens em vetores numéricos.

4. **Treinamento da rede de classificação**  
   Rede treinada para identificar a classe correta entre as 4 categorias.

5. **Sistema de recomendação visual**  
   Busca por similaridade com base nos embeddings e na classe prevista.

---

## ▶️ Como Executar o Projeto

Este projeto foi desenvolvido e testado no Google Colab. Siga os passos abaixo para executá-lo:

### Passo 1: Configure o Ambiente

1.  Clone este repositório para o seu ambiente local ou copie os arquivos para o Google Colab.
2.  Instale as dependências necessárias com o `pip` (se estiver fora do Colab):

    ```bash
    pip install tensorflow scikit-learn matplotlib Pillow
    ```
3.  Abra o notebook `sistema_recomendacao.ipynb` no Google Colab.

### Passo 2: Prepare o Dataset

1.  Faça o upload de suas imagens para cada uma das categorias no Colab, usando o código `from google.colab import files` conforme indicado no notebook.

2.  Aplique a técnica de data augmentation para gerar imagens aumentadas.

### Passo 3: Treine o Modelo e Gere o Sistema de Recomendação

1.  Execute as células do notebook para extrair os embeddings das imagens. O sistema irá gerar os arquivos `embeddings.npy` e `image_paths.json`.

2.  Treine o modelo de classificação com o comando:
    ```python
    history = model.fit(train_gen, validation_data=val_gen, epochs=10)
    ```

---

### Passo 4: Teste com uma Imagem Externa

1.  Faça o upload de uma imagem externa que você queira testar.
2.  Use a função `classify_image()` para classificar a imagem na rede:
    ```python
    classify_image("nome_da_imagem.jpeg")
    ```
3.  Use a função `recommend_by_class_and_similarity()` para obter as recomendações:
    ```python
    recommend_by_class_and_similarity("nome_da_imagem.jpeg")
    ```

---

## 📋 Resultados Esperados

- A imagem enviada será classificada em uma das 4 categorias (`camiseta`, `sapato`, `relógio`, `bolsa`).
- O sistema retornará as imagens mais semelhantes visualmente dentro da mesma classe prevista.

---

## ❤️ Como Contribuir ou Apoiar

Se este repositório foi útil para você, considere dar uma **estrela** ⭐️ no canto superior direito para me apoiar. Isso me motiva a continuar criando conteúdo e projetos de qualidade.

Se você deseja usar este projeto como base para o seu próprio trabalho ou propor melhorias, sinta-se à vontade para dar um **fork** no repositório.

1. **Faça o Fork**: Clique no botão "Fork" no canto superior direito desta página.
2. **Clone o Repositório**: Clone o seu fork para sua máquina local.
3. **Faça suas Alterações**: Crie uma nova branch, faça suas alterações e suba o código.
4. **Abra um Pull Request**: Envie um Pull Request para que suas alterações possam ser revisadas e, se aprovadas, mescladas ao projeto original.





