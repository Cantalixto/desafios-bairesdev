# Agente de IA para Geração de Testes Unitários com OpenAI e Pytest

## Descrição do Projeto

Este projeto é uma entrega para o Bootcamp DIO e BairesDev, demonstrando a construção de um agente de software capaz de gerar testes unitários automaticamente a partir de um código-fonte em Python.

A solução explora conceitos de **Prompt Engineering**, usando a **API da OpenAI** para analisar o código e criar testes unitários com a biblioteca **pytest**.

## Conceitos-Chave

- **Prompt Engineering:** A arte de criar instruções claras e precisas para modelos de Inteligência Artificial, garantindo que a resposta gerada seja de alta qualidade e alinhada com o objetivo.
- **OpenAI API:** A interface de programação que permite que o agente se comunique com os modelos de linguagem da OpenAI, como o GPT-3.5 Turbo.
- **Pytest:** Um framework de testes em Python que é simples e poderoso, ideal para a escrita de testes unitários.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos e sua respectiva função:

- `main.py`: Contém a lógica principal do agente. Ele lê um arquivo de código, envia o conteúdo para a API da OpenAI com um prompt detalhado e salva a resposta (o código dos testes) em um novo arquivo.
- `funcoes_exemplo.py`: Um arquivo com funções de exemplo (`soma` e `subtrair`) que serve como entrada para o agente de IA.
- `requirements.txt`: Lista as bibliotecas Python necessárias para o projeto (`openai`, `python-dotenv`, `pytest`).
- `.env`: Arquivo para armazenar com segurança a chave de API da OpenAI, garantindo que ela não seja exposta publicamente.

## Como Executar o Agente

### Passo 1: Configuração do Ambiente

1.  Clone este repositório para a sua máquina.
2.  Navegue até a pasta do projeto no terminal.
3.  Instale as dependências necessárias com o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```

### Passo 2: Configuração da Chave de API

Para usar a API da OpenAI, você precisa de uma chave. Siga estas instruções para configurá-la:

1.  Crie uma conta na [plataforma da OpenAI](https://platform.openai.com/).
2.  Gere uma nova chave secreta na seção [API keys](https://platform.openai.com/api-keys).
3.  Na raiz do projeto, crie um arquivo chamado `.env`.
4.  Adicione a sua chave de API neste arquivo, no formato a seguir. **Substitua o texto pela sua chave.**

    ```
    OPENAI_API_KEY="sua_chave_de_api_aqui"
    ```

> **Atenção:** Nunca compartilhe este arquivo ou a sua chave publicamente!

### Passo 3: Execução do Agente

Com as dependências instaladas e a chave de API configurada, você pode executar o agente com o seguinte comando:

```bash
python main.py
```

Se a sua API e os créditos de uso estiverem ativos, o script irá:

1. Ler o código em `funcoes_exemplo.py`.
2. Gerar os testes correspondentes usando a API da OpenAI.
3. Salvar o resultado em um novo arquivo chamado `test_funcoes_exemplo.py`.

### Passo 4: Rodando os Testes Gerados

Para verificar se os testes criados pela IA estão corretos, use o pytest no terminal:

```bash
pytest
```

## Reflexões e Aprendizados
A criação deste projeto foi uma jornada de aprendizado prático que reforçou a importância de conceitos essenciais no desenvolvimento moderno. A experiência me mostrou que o Prompt Engineering é a alma de um agente de IA, pois a qualidade da resposta gerada depende diretamente da clareza e precisão das instruções fornecidas ao modelo.

Além disso, pude entender a diferença entre a API pública da OpenAI e o serviço Azure OpenAI. Enquanto a API pública é ideal para prototipagem e testes rápidos, o Azure oferece uma solução mais robusta e controlada para ambientes corporativos, com suas próprias particularidades de configuração. A dificuldade com o erro de "quota" foi uma lição valiosa sobre a dependência de serviços externos e a importância de saber como diagnosticar e lidar com falhas em tempo real, um desafio comum na vida de qualquer desenvolvedor.