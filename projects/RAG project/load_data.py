from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import key_params

client = MongoClient(key_params.MONGO_URI)
dbName = 'lancgahin_demo'
collectionName = 'collection_of_text_blobs'
collection = client[dbName][collectionName]

loader = DirectoryLoader('./sample', glob='./*.txt', show_progress=True)
data = loader.load()

embeddings = OpenAIEmbeddings(openai_api_key=key_params.API_KEY)


