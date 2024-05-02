from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.llms import openai
from langchain.chains.retrieval_qa.base import RetrievalQA
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


