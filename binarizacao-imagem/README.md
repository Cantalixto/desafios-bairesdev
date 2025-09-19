# 🖼️  Desafio de Projeto: Redução de Dimensionalidade em Imagens para Redes Neurais

Este projeto realiza a binarização de uma imagem colorida utilizando **apenas funções nativas do Python**, sem o uso de bibliotecas específicas de processamento de imagem como OpenCV ou NumPy. O objetivo é compreender os fundamentos da manipulação de pixels e da aplicação de limiar.

---

## ⚙️ Etapas do Processamento

1. **Abrir imagem RGB**
2. **Converter para tons de cinza**
3. **Aplicar binarização com limiar definido**

> Todo o processamento é feito em tempo de execução, sem salvar versões intermediárias da imagem.

---

## 📦 Requisitos

- Python 3.6+
- [Pillow](https://pypi.org/project/Pillow/) → `pip install pillow`  
- [Matplotlib](https://pypi.org/project/matplotlib/) → `pip install matplotlib`

---

## 📂 Estrutura do Projeto

```bash
binarizacao-imagem/
├── binarizacao_imagem.py
├── lena.png
└── README.md
```

---

## ▶️ Como Executar o Projeto

### Passo 1: Clone o Repositório
Para obter o código do projeto, use o comando `git clone` no seu terminal:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
python binarizacao.py
```

Em seguida, navegue até a pasta específica do projeto:
```bash
cd desafios-bairesdev/binarizacao-imagem
```

### Passo 2: Instale as Dependências
Este projeto requer as bibliotecas Pillow e Matplotlib. Você pode instalá-las usando o pip:
```bash
pip install Pillow Matplotlib
```

### Passo 3: Execute o Código
Para rodar o script e ver o resultado da binarização, execute o seguinte comando:
```bash
python binarizacao_imagem.py
```
---

## 📸 Imagem Utilizada

A imagem original utilizada é a clássica `lena.png`:

![Lena Colorida](lena.png)

---

## ❤️ Como Contribuir ou Apoiar

Se este repositório foi útil para você, considere dar uma estrela ⭐️ no canto superior direito para me apoiar. Isso me motiva a continuar criando conteúdo e projetos de qualidade.

Se você deseja usar este projeto como base para o seu próprio trabalho ou propor melhorias, sinta-se à vontade para dar um fork no repositório.
1. Faça o Fork: Clique no botão "Fork" no canto superior direito desta página.
2. Clone o Repositório: Clone o seu fork para sua máquina local.
3. Faça suas Alterações: Crie uma nova branch, faça suas alterações e suba o código.
4. Abra um Pull Request: Envie um Pull Request para que suas alterações possam ser revisadas e, se aprovadas, mescladas ao projeto original.


