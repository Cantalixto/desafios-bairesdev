# 🖼️ Binarização de Imagem com Funções Puras em Python

Este projeto realiza a binarização de uma imagem colorida utilizando **apenas funções nativas do Python**, sem o uso de bibliotecas específicas de processamento de imagem como OpenCV ou NumPy. O objetivo é compreender os fundamentos da manipulação de pixels e da aplicação de limiar.

## ⚙️ Etapas do Processamento

1. **Abrir imagem RGB**
2. **Converter para tons de cinza**
3. **Aplicar binarização com limiar definido**

> Todo o processamento é feito em tempo de execução, sem salvar versões intermediárias da imagem.

## 📸 Imagem Utilizada

A imagem original utilizada é a clássica `lena.png`:

![Lena Colorida](lena.png)

## 📦 Requisitos

- Python 3.6+
- [Pillow](https://pypi.org/project/Pillow/) → `pip install pillow`  
- [Matplotlib](https://pypi.org/project/matplotlib/) → `pip install matplotlib`

## ▶️ Como Executar

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
python binarizacao.py
