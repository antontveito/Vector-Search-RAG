import pymongo
import openai
import os

from dotenv import load_dotenv
load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')
API_KEY =  os.getenv('OPEN_AI_API_KEY')

openai.api_key = API_KEY

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.sample_mflix
collection = db.embedded_movies

def generate_embedding(text: str) -> list[float]:
    response = openai.Embedding.create(
        model="text-embedding-ada-002", 
        input=text
    )
    return response['data'][0]['embedding']



query = 'Aliens from outer space invade the world'

results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embedding(query),
    "path": "plot_embedding",
    "numCandidates": 100,
    "limit": 1,
    "index": "PlotSemanticSearch",
      }}
])

print(results)

for document in results:
    print('Hello')
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')