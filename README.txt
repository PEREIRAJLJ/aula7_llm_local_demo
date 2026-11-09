ML III — Aula 7
Aplicações com Large Language Models — Mistral Local

1. INSTALAR O OLLAMA
O Ollama é um programa que permite executar Large Language Models
localmente no computador.
IMPORTANTE:
O Ollama NÃO é uma biblioteca Python. Portanto, ele não é instalado
pelo requirements.txt e não depende do ambiente Conda "ml".

1.1 Baixar o Ollama
Acesse:
https://ollama.com/download
Escolha a versão para Windows e faça a instalação normalmente.
1.2 Verificar a instalação
Após a instalação, abra um NOVO terminal (CMD ou terminal do VS Code)
e execute:
ollama --version
Se aparecer a versão instalada, o Ollama está funcionando.
Exemplo:
ollama version 0.x.x

2. BAIXAR O MODELO MISTRAL
Instalar o Ollama não instala automaticamente todos os modelos.
Execute:
ollama pull mistral
O Ollama fará o download do modelo para o computador.
ATENÇÃO:
O download possui alguns GB e pode demorar dependendo da conexão.

3. VERIFICAR OS MODELOS INSTALADOS
Execute:
ollama list
Deverá aparecer "mistral" entre os modelos disponíveis.

4. TESTAR O MISTRAL DIRETAMENTE
Antes de executar nosso código Python, vamos verificar se o modelo
está funcionando.
Execute:
ollama run mistral
O terminal ficará disponível para conversa com o modelo.
Exemplo:
>>> O que é Machine Learning?
O Mistral deverá gerar uma resposta diretamente no terminal.
Para encerrar a conversa:
/bye

5. INSTALAR AS DEPENDÊNCIAS PYTHON
Agora utilizaremos nosso ambiente Python.
Abra o terminal do VS Code e confirme que o ambiente "ml" está ativo:
(ml)
Execute:
cd "C:\Users\User\Documents\1 - ENGENHARIA\1 - DOCÊNCIA\1 - AULAS\3 - ML III\AULA 7\aula7_llm_local_demo"
pip install -r requirements.txt

6. INICIAR A API
Execute:
python -m uvicorn api:app --reload
A API ficará disponível em:
http://127.0.0.1:8000
Documentação automática:
http://127.0.0.1:8000/docs

5. EXECUTAR A APLICAÇÃO
Abra outro terminal com o ambiente `ml` ativo.
Entre novamente na pasta:
cd "C:\Users\User\Documents\1 - ENGENHARIA\1 - DOCÊNCIA\1 - AULAS\3 - ML III\AULA 7\aula7_llm_local_demo"
Execute:
python -m streamlit run app.py

6. ABRIR A APLICAÇÃO
Acesse:
http://localhost:8501

Como a memória funciona?
A aplicação mantém uma lista de mensagens durante a sessão:
[
{"role": "system", "content": "..."},
{"role": "user", "content": "O que é Random Forest?"},
{"role": "assistant", "content": "..."},
{"role": "user", "content": "E qual a principal vantagem dele?"}
]

A cada nova pergunta, o histórico completo é enviado novamente ao modelo.
Isso permite que o Mistral interprete expressões como "dele", "isso" e "o anterior" usando o contexto da conversa.
Observação
O modelo roda localmente via Ollama. Portanto:
não há cobrança por chamada de API;
o desempenho depende do computador;
o modelo ocupa espaço em disco;
a primeira resposta pode demorar mais enquanto o modelo é carregado para a memória.