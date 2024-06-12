import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyMuPDFLoader
from dotenv import load_dotenv

from flask import Flask, jsonify, request

app = Flask(__name__)

load_dotenv()

# init the rag
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
persist_directory = 'db'
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

vectordb = Chroma(persist_directory=persist_directory, 
                  embedding_function=embedding)

retriever = vectordb.as_retriever(search_kwargs={"k": 2})

qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), 
                                  chain_type="stuff", 
                                  retriever=retriever, 
                                  return_source_documents=True)


# Main route
@app.route('/')
def main():
    return 'Health check!'

# ask chatbot endpoint
@app.route('/ask', methods=['POST'])
def ask():
    query = request.get_json().get('question')
    llm_response = qa_chain.invoke(query)

    return 'Answer: ' + llm_response['result']

# if __name__ == '__main__':
#     app.run(debug=True)