# Chatbot do Colégio COTUCA

Bem-vindo ao Chatbot do Colégio Cotuca! Este projeto visa fornecer informações rápidas e úteis sobre o colégio, abrangendo uma variedade de tópicos, como cursos, departamentos, estágios, datas de vestibulares, e muito mais. O chatbot foi desenvolvido utilizando Django para o back-end e HTML, CSS, e REACT para o front-end. A interação do chatbot é alimentada pela API do OpenAI e treinada usando a biblioteca Llama-Index.

## Configuração do Ambiente

Certifique-se de ter Python instalado no seu sistema. Você pode instalar as dependências necessárias utilizando o seguinte comando:

```bash

Configuração do Django
1 - Crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual:
No Windows:
venv\Scripts\activate

No Linux/Mac:
source venv/bin/activate

Instale as dependências do Django:
pip install django

Execute as migrações do banco de dados:
python manage.py migrate

Inicie o servidor:
python manage.py runserver

O seu servidor estará disponível em http://localhost:8000

Configuração da API do OpenAI
Obtenha sua chave de API do OpenAI.

Adicione a chave ao arquivo .env na raiz do projeto:


OPENAI_API_KEY=SuaChaveAqui

Treinamento do Chatbot
Utilize a biblioteca Llama-Index para treinar o chatbot com dados específicos do colégio.

# Exemplo de código para treinamento
from llama_index import LlamaIndex

llama = LlamaIndex()
llama.train("dados_do_colegio.txt")
Substitua "dados_do_colegio.txt" pelo caminho do arquivo de treinamento contendo perguntas e respostas específicas do colégio.

Utilização do Chatbot
Acesse o site em http://localhost:8000/ e comece a interagir com o Chatbot para obter informações sobre o colégio.
