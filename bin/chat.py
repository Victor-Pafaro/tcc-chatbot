import os # Sistema operacional, para colocarmos OpenAI como variavel de ambiente
from llama_index import TreeIndex, SimpleDirectoryReader

class Chat:

    def __init__(self):
        self.pergunta = None
        self.query_engine = None

    def get_resposta(self):
        response =  self.query_engine.query(self.pergunta)
        return response

    def treino(self):
<<<<<<< HEAD
        os.environ["OPENAI_API_KEY"] = "chave-token-aqui"
=======
        os.environ["OPENAI_API_KEY"] = "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"
>>>>>>> eb95c1d429fe1eee17b6ad8822e5ff1ffb4c85d9

        path = os.path.join(os.path.abspath("."),"bin", "artigos")
        print(path)

        documents = SimpleDirectoryReader(path).load_data()  # Carrega na memoria todos os arquivos do diretorio artigos.
        index = TreeIndex.from_documents(documents)  # Cria um indice para todos os termos dos documentos

        self.query_engine = index.as_query_engine()  # Alimenta o motor de busca com os documentos fornecidos.