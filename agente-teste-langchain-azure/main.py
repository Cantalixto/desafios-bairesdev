# main.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# --- Configuração e Inicialização ---
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente da OpenAI, usando a chave que está no arquivo .env
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    print(f"Erro ao inicializar o cliente OpenAI: {e}")
    print("Verifique se a sua chave de API está configurada corretamente no arquivo .env.")
    exit()

# --- Lógica do Agente de IA ---
def gerar_testes_pytest(codigo_string):
    # Usa um modelo de IA para gerar testes unitários pytest para um código Python.
    # O código dos testes é retornado como uma string.
    
    # Prompt de engenharia: as instruções detalhadas para a IA
    prompt = f"""
Você é um especialista em testes de software. Sua tarefa é gerar testes unitários
com pytest para o código Python fornecido. Crie testes para casos de sucesso e casos de falha/exceção.

**Instruções para a saída:**
- O código deve ser em Python puro.
- A primeira linha deve ser 'import pytest'.
- As funções de teste devem seguir o padrão 'def test_*'.
- Use 'assert' para verificar o resultado.
- Use 'pytest.raises' para casos que esperam uma exceção.

**Código a ser testado:**
{codigo_string}
    """

    # Faz a requisição à API da OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil para gerar testes de código."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API da OpenAI: {e}")
        return ""

# --- Função Principal para Executar o Agente ---
def main():
    # Lê um arquivo de código, gera os testes e salva o resultado.
    source_file = "funcoes_exemplo.py"
    
    if not os.path.exists(source_file):
        print(f"Erro: O arquivo '{source_file}' não foi encontrado.")
        return

    with open(source_file, "r") as f:
        code_para_testar = f.read()

    print(f"Gerando testes para o arquivo: {source_file}...")
    
    testes_gerados = gerar_testes_pytest(code_para_testar)
    
    if not testes_gerados:
        print("Não foi possível gerar os testes. Verifique a sua conexão e a chave de API.")
        return

    test_file_name = f"test_{os.path.basename(source_file)}"
    
    with open(test_file_name, "w") as f:
        f.write(testes_gerados)
        
    print(f"Testes gerados com sucesso no arquivo: {test_file_name}")
    print("\nPara rodar os testes, use o comando: pytest")

if __name__ == "__main__":
    main()