from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.llms import openai
from langchain.chains.retrieval_qa.base import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import key_params
