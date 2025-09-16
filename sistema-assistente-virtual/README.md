# 🧠 Assistente Virtual com Reconhecimento de Voz e Resposta em Áudio

Este projeto é um assistente virtual simples desenvolvido em Python, capaz de **ouvir comandos de voz**, **interpretá-los** e **responder com áudio**, além de executar ações automatizadas como abrir o YouTube ou informar a hora atual.

## 🎯 Objetivo

Criar um sistema de assistência virtual que combine:
- Reconhecimento de fala (Speech-to-Text)
- Síntese de fala (Text-to-Speech)
- Execução de comandos automatizados

## 🛠️ Tecnologias Utilizadas

- `gTTS` – Google Text-to-Speech para gerar áudio
- `playsound` – reprodução de arquivos de áudio (em ambientes locais)
- `speech_recognition` – reconhecimento de voz via microfone
- `pytz` e `datetime` – para exibir a hora correta em Brasília
- `webbrowser` – para abrir links automaticamente
- `IPython.display.Audio` – reprodução de áudio no Jupyter/Colab

## 📦 Instalação

Instale as bibliotecas necessárias com os comandos abaixo:

```bash
pip install gTTS
pip install playsound
pip install SpeechRecognition
```

⚠️ Importante: O reconhecimento de voz via microfone não funciona no Google Colab, pois ele não tem acesso ao hardware local. Para usar o microfone, execute o projeto em um ambiente local como Jupyter Notebook, VS Code ou terminal.

---
## 📂 Estrutura do Projeto

### 🔊 `falar(texto)`
Converte texto em áudio e reproduz automaticamente.

### ❓ `perguntar(pergunta)`
Recebe uma pergunta do usuário e responde com áudio.

### ⚙️ `executar_comando(comando)`
Interpreta comandos como:

- `"Abrir o YouTube"` → abre o site e responde com áudio  
- `"Que horas são?"` → informa a hora atual em Brasília

### 🎙️ `ouvir_comando()`
Captura áudio do microfone e converte em texto usando o Google Speech Recognition.

## 🔁 Fluxo de Execução

O assistente segue o seguinte fluxo:

1. Captura o comando de voz do usuário via microfone.
2. Converte o áudio em texto usando a API do Google Speech Recognition.
3. Interpreta o comando e executa a ação correspondente.
4. Responde com áudio gerado via gTTS.

```python
comando_voz = ouvir_comando()
if comando_voz:
    executar_comando(comando_voz)
```

---

## 🧪 Exemplos de Uso
```
falar("Olá! Eu sou seu assistente virtual.")
executar_comando("Abrir o YouTube")
executar_comando("Que horas são?")
```

---
## 🚧 Limitações

- O microfone não funciona no Google Colab.
- O reconhecimento de voz depende de conexão com a internet.
- O projeto ainda não inclui busca no Wikipedia ou localização de farmácias (pode ser expandido futuramente).

## 📚 Recursos Adicionais

- [gTTS – Google Text-to-Speech](https://pypi.org/project/gTTS/)
- [SpeechRecognition – PyPI](https://pypi.org/project/SpeechRecognition/)
- [Text-to-Speech DIO – GitHub](https://github.com/diegobrunoDIO/Text-to-Speech-DIO)






