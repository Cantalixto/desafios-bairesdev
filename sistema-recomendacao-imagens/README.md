# Sistema de Recomendação por Imagens Digitais

## Objetivo

Este projeto tem como objetivo desenvolver um sistema de recomendação visual utilizando deep learning. A proposta envolve:

- Treinar uma rede neural com **4 classes de objetos**: `camiseta`, `sapato`, `relógio`, `bolsa`
- Utilizar **transfer learning** com EfficientNetB0
- Implementar recomendação por **similaridade visual** com base na classe prevista
- Permitir que o usuário envie uma imagem externa e receba sugestões visuais semelhantes

---

## Tecnologias utilizadas

- Python 3
- TensorFlow / Keras
- EfficientNetB0 (pré-treinado no ImageNet)
- Scikit-learn
- Matplotlib
- Pillow

---

## Etapas do projeto

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

##  Como rodar o projeto

Este projeto foi desenvolvido e testado no Google Colab.

1. Clone o repositório ou copie os arquivos para o Colab
   
2. Envie imagens para cada categoria
```python
upload_to("camiseta")
upload_to("sapato")
upload_to("relogio")
upload_to("bolsa")
```

3. Aplique data augmentation
```python
for cat in ["camiseta", "sapato", "relogio", "bolsa"]:
    augment_images(cat, n_aug=5)
```

4. Extraia os embeddings das imagens aumentadas
O sistema irá gerar os arquivos embeddings.npy e image_paths.json
Esses arquivos serão usados para calcular similaridade visual

5. Treine o modelo de classificação
```
history = model.fit(train_gen, validation_data=val_gen, epochs=10)
```

---

## Teste com imagem externa

1. Faça upload da imagem para o Colab:
```
from google.colab import files
uploaded = files.upload()
```

2. Classifique a imagem:
```
classify_image("nome_da_imagem.jpeg")
```

3. Recomende imagens semelhantes dentro da mesma classe:
```
recommend_by_class_and_similarity("nome_da_imagem.jpeg")
```

---

## Resultados esperados
- A imagem enviada será classificada em uma das 4 categorias.
- O sistema retornará as imagens mais semelhantes visualmente dentro da mesma classe prevista.

---

## Observações
- As imagens originais e aumentadas não estão incluídas no repositório.
O usuário deve fazer o upload manualmente no Colab usando a função upload_to("categoria").
- O projeto foi desenvolvido para fins acadêmicos e pode ser adaptado para outros domínios visuais.









