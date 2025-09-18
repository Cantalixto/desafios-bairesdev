# Criando um Agente para Detecção de Vulnerabilidades em Arquiteturas
Este projeto é a minha entrega para o desafio do Bootcamp DIO e BairesDev, focado em documentar a criação de um agente de software para análise de ameaças em arquiteturas de aplicações.

A solução explora a metodologia STRIDE e os conceitos de Prompt Engineering, demonstrando a capacidade de usar a Inteligência Artificial para gerar análises de segurança de forma automatizada.

---

## Conceitos-Chave
Este projeto foi construído sobre alguns pilares importantes da programação moderna e da segurança da informação.

### FastAPI: Um framework web de alto desempenho em Python, ideal para construir APIs de forma rápida e com documentação automática. Ele foi usado para criar a interface que recebe a imagem e retorna a análise de ameaças.

### Prompt Engineering: A arte de criar instruções claras e eficazes para modelos de IA. No contexto deste projeto, um prompt bem-definido seria enviado a um modelo de IA para que ele analisasse a imagem de arquitetura e identificasse as ameaças de forma precisa.

### Metodologia STRIDE: Uma estrutura de análise de ameaças de segurança que classifica vulnerabilidades em seis categorias:

Spoofing: Falsificação de identidade.

Tampering: Alteração de dados.

Repudiation: Ações que não podem ser rastreadas.

Information Disclosure: Vazamento de informações.

Denial of Service: Ataques que impedem o uso do serviço.

Elevation of Privilege: Elevação de privilégios de um usuário.

---

## Estrutura da Solução
A arquitetura do agente de detecção de ameaças seguiria o seguinte fluxo:

Recebimento da Imagem: A API, construída com FastAPI, recebe uma imagem de um diagrama de arquitetura de software via upload.

Envio para o Modelo de IA: A imagem e um prompt bem elaborado seriam enviados ao serviço Azure OpenAI.

Análise e Geração de Texto: O modelo de IA processaria a imagem e o prompt, gerando uma análise detalhada das ameaças com base na metodologia STRIDE.

Processamento da Resposta: A API receberia a resposta textual do modelo e a processaria, formatando-a de forma estruturada.

Geração do Relatório: A análise formatada seria retornada como resposta da API, permitindo que a aplicação consumidora a exiba de forma clara.

## Como Executar a Demonstração
Para testar o código de exemplo que simula a API, siga as instruções abaixo:

Instalar as Dependências:
Certifique-se de que o Python está instalado e, a partir da raiz do projeto, execute o comando para instalar as bibliotecas necessárias:
```
Bash

pip install -r requirements.txt
```

Executar a API:
Inicie o servidor local do FastAPI com o seguinte comando:

```
Bash

uvicorn main:app --reload
```

Acessar a Documentação Interativa:
Abra seu navegador e acesse o endereço http://127.0.0.1:8000/docs. Lá, você poderá testar o endpoint de análise de ameaças (/analyze_threats/) e ver a resposta simulada.

Ao final deste projeto, pude aprofundar meu conhecimento em FastAPI, entender a importância da metodologia STRIDE para a segurança e aplicar conceitos de Prompt Engineering em um cenário prático e relevante.
